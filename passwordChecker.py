from pathlib import Path
from difflib import SequenceMatcher

PASSWORDS_PATH = Path("passwords.txt")

def loadCommonPasswords(path: Path) -> list[str] :
    if not path.exists():
        raise FileNotFoundError("Passwords list cannot be found")
    
    passwords = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                passwords.append(stripped)

    return passwords

def checkCharDiversity(password: str) -> dict[str, bool]:
    return {
        "lower": any(c.islower() for c in password),
        "upper": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "symbol": any(not c.isalnum() for c in password),
    }

def checkCommonResemblence(password: str, common: list[str]) -> tuple[float, str]:
    candidates = []
    passwordLen = len(password)
    for pw in common:
        if abs(len(pw) - passwordLen) <= 2:
            candidates.append(pw)

    closestRatio = 0.0
    closestMatch = ""
    for pw in candidates:
        ratio = SequenceMatcher(None, pw, password).ratio()
        if ratio > closestRatio:
            closestRatio = ratio
            closestMatch = pw

    return closestRatio, closestMatch

def scorePassword(password: str, diversity: dict[str, bool], resemblance: float) -> int:
    score = 0

    # Length (Max 4pts)
    length = len(password)
    if length >= 20:
        score += 4
    elif length >= 10:
        score += 2
    elif length >= 8:
        score += 1

    # Diversity (Max 4pts)
    for k in diversity.values():
        if k:
            score += 1

    # Common Matches
    if resemblance >= 0.75:
        score -= 4
    elif resemblance >= 0.5:
        score -= 3
    elif resemblance >= 0.25:
        score -= 1

    return max(0, min(10, score))

def main():
    common = loadCommonPasswords(Path("passwords.txt"))

    pw = input("Enter a password to check strength: ").rstrip("\n")
    if not pw:
        print("No input")
        return
    
    charDiversity = checkCharDiversity(pw)
    resemblance, closest = checkCommonResemblence(pw, common)

    score = scorePassword(pw, charDiversity, resemblance)

    # Print Report section
    print("\n-----Report-----")
    print(f"Length: {len(pw)}")
    print(f"Character Diversity: \n",
          f"    Lowercase: {'Yes' if charDiversity['lower'] else 'No'}\n",
          f"    Uppercase: {'Yes' if charDiversity['upper'] else 'No'}\n",
          f"    Numbers: {'Yes' if charDiversity['digit'] else 'No'}\n",
          f"    Special: {'Yes' if charDiversity['symbol'] else 'No'}\n",)
    
    if resemblance >= 0.25:
        print(f"Resemblance to a common password: {resemblance * 100}%.\n"+
              f"    Closest Match: {closest}.\n")
        
    print(f"Total Score (0-10): {score}")

if __name__ == "__main__":
    main()