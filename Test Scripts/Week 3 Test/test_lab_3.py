import importlib
import subprocess
import sys
from difflib import SequenceMatcher

def test_main(tester: str, proctor: str, dynImport) -> None:
    # STDOUT Test
    print("\n\n{:<10}{:^50}{:^60}{:<30}{:<10}\n".format('Result', 'Test Print', 'Proctor Print','Sequence', 'Certainty'))
    results1 = test_printout(tester, proctor)
    print_results('PRINTOUT', results1)

    # Import test
    if dynImport is None:
        print("Skipping IMPORT TEST as dynImport is None")
    else:
        print("\n\n{:<10}{:<10}\n".format('Result', 'Function', ))
        results2 = test_import(dynImport)
        print_results('IMPORT', results2)

def print_results(test: str, scores: list):
    print(f"""\n{test} RESULTS:
\t{'Correct:':<15}{scores.count(True)}
\t{'Incorrect:':<15}{scores.count(False)}
\t{'Accuracy:':<15}{scores.count(True)/len(scores):0.1%}""")

def test_printout(tester, proctor):
    scores = []

    seqList = [
        ['add'],
        ['add', '2', '-3.5', '2.5', '-1.5'],
        ['subtract', '2', '-3.5', '2.5', '-1.5'],
        ['multiply', '2', '-3.5', '2.5', '-1.5'],
        ['divide', '2', '-3.5', '2.5', '-1.5'],
        ['test', '2', '-3.5', '2.5', '-1.5'],
        ['add', '1', '2'],
        ['subtract', '1', '2'],
        ['divide', '0', '1', '0'],
        ['divide', '0', '1', '2']
    ]

    for sequence in seqList:
        scores.append(test_compare_outputs(tester, proctor, sequence))

    return scores


def test_import(dynImport):
    try:
        importlib.invalidate_caches()
        imported = importlib.import_module('..'+dynImport, 'test.subpkg')
    except ImportError:
        input(f"WARNING: {dynImport}.py not found not found in ./test, make sure you typed the name in correctly.\nIf it was make sure it is in ./test. Enter to exit...")
        sys.exit()
    
    scores = []
    functions = ['add', 'divide', 'subtract', 'multiply']
    for func in functions:
        try:
            getattr(imported, func)([4, 5])
            print(f"{'PASS':<10}{func:<30}")
            scores.append(True)
        except AttributeError:
            print(f"{'FAIL':<10}{func:<10}")
            scores.append(False)

    return scores

def test_compare_outputs(tester, proctor, testSequence):
    process = subprocess.Popen(['python', tester,  *testSequence], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    testerOut = process.stdout.read().decode('utf-8').strip()
    process = subprocess.Popen(['python', proctor,  *testSequence], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    proctorOut = process.stdout.read().decode('utf-8').strip()

    combinedResults = f"{testerOut[:50]:<50} | {proctorOut[:50]:<50}"
    similarity = similar(proctorOut, testerOut)
    if similarity > .98:
        print(f"{'PASS':<10}{combinedResults}| {' '.join(testSequence):<30}| {similarity}")
        return True
    else:
        print(f"{'FAIL':<10}{combinedResults}| {' '.join(testSequence):<30}| {similarity}")
        return False
    
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()