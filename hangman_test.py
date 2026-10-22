import subprocess

APP = "/Users/antoniopascarella/Uni/SWTEST/hangman_buggy_2"


def stop_game(process):
    if process.poll() is None:
        process.terminate()
        process.wait()


# 1. VALIDITY TESTS OF SECRET WORD FORMATTING


print("TEST 1.1: secret word cannot have less than 3 letters")

process = subprocess.Popen(
    [APP, "ab"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

result = process.stdout.readline().strip()

if result.startswith("ERROR"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 1.2: secret word cannot contain uppercase letters")

process = subprocess.Popen(
    [APP, "Testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

result = process.stdout.readline().strip()

if result.startswith("ERROR"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 1.3: secret word cannot contain numbers")

process = subprocess.Popen(
    [APP, "test1ng"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

result = process.stdout.readline().strip()

if result.startswith("ERROR"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 1.4: secret word with exactly 3 lowercase letters is accepted")

process = subprocess.Popen(
    [APP, "abc"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

result = process.stdout.readline().strip()

if result.startswith("You have to guess"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 1.5: scrambled word must have the same number of dots as the secret word")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

result = process.stdout.readline().strip()

if result == "You have to guess the following word: .......":
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


# 2. CHARACTER/WORDS GUESSING TESTS


print("TEST 2.1: uppercase guess gives an error")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("A\n")
process.stdin.flush()

result = process.stdout.readline().strip()

if result.startswith("ERROR"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 2.2: guess containing a number gives an error")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("a1\n")
process.stdin.flush()

result = process.stdout.readline().strip()

if result.startswith("ERROR"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 2.3: guess with wrong word length gives an error")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("test\n")
process.stdin.flush()

result = process.stdout.readline().strip()

if result.startswith("ERROR"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 2.4: correct single-letter guess reveals all occurrences of that letter")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("t\n")
process.stdin.flush()

process.stdout.readline()
result = process.stdout.readline().strip()

if result.startswith("You have to guess the following word: t..t"):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 2.5: wrong full-word guess counts as 1 mistake")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("ttttttt\n")
process.stdin.flush()

result = process.stdout.readline().strip()

if result.startswith("That's not the correct word."):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 2.6: wrong single-letter guess counts as 1 mistake")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("a\n")
process.stdin.flush()

result = process.stdout.readline().strip()

if result.startswith("That letter is not correct."):
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)



# 3. WIN/LOSE VALIDITY AND PARTICULAR TESTS


print("TEST 3.1: guessing the whole correct word wins")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("testing\n")
process.stdin.flush()

result = process.stdout.readline().strip()

if result == "You won, congratulations!":
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 3.2: guessing all letters individually wins")

process = subprocess.Popen(
    [APP, "abc"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("a\n")
process.stdin.flush()

process.stdout.readline()
process.stdout.readline()
process.stdout.readline()

process.stdin.write("b\n")
process.stdin.flush()

process.stdout.readline()
process.stdout.readline()
process.stdout.readline()

process.stdin.write("c\n")
process.stdin.flush()

result = process.stdout.readline().strip()

if result == "You won, congratulations! The secret word was abc.":
    print("PASS")
else:
    print("FAIL")
    print("Output was:", result)

stop_game(process)


print("TEST 3.3: after 5 wrong guesses the user loses")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

wrong_guesses = ["a", "b", "c", "d", "f"]
last_result = ""

for guess in wrong_guesses:
    process.stdin.write(guess + "\n")
    process.stdin.flush()

    last_result = process.stdout.readline().strip()

    if "You lost" not in last_result:
        process.stdout.readline()
        process.stdout.readline()

if last_result == "You lost. The secret word was testing.":
    print("PASS")
else:
    print("FAIL")
    print("Output was:", last_result)

stop_game(process)



print("TEST 3.4: game should stop after winning")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

process.stdin.write("testing\n")
process.stdin.flush()

process.stdout.readline()

process.wait()

if process.poll() is not None:
    print("PASS")
else:
    print("FAIL")

if process.poll() is None:
        process.terminate()
        process.wait(timeout=1)


print("TEST 3.5: game should stop after losing")

process = subprocess.Popen(
    [APP, "testing"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

process.stdout.readline()
process.stdout.readline()

wrong_guesses = ["a", "b", "c", "d", "f"]

for guess in wrong_guesses:
    process.stdin.write(guess + "\n")
    process.stdin.flush()

    result = process.stdout.readline().strip()

    if "You lost" not in result:
        process.stdout.readline()
        process.stdout.readline()

if process.poll() is not None:
    print("PASS")
else:
    print("FAIL")

if process.poll() is None:
        process.terminate()
        process.wait(timeout=1)
