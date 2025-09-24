import sys

def match_pattern(input_line, pattern):
    """Main function to match pattern anywhere in input_line"""
    if not pattern:
        return True
    
    if pattern.startswith('^'):
        return match_here(input_line, pattern[1:])
    
    for i in range(len(input_line) + 1):
        if match_here(input_line[i:], pattern):
            return True
    return False

def match_here(input_line, pattern):
    """Match pattern at the beginning of input_line"""
    if not pattern:
        return True
    
    if len(pattern) >= 2 and pattern[1] == '*':
        return match_star(pattern[0], pattern[2:], input_line)
    
    if pattern == '$':
        return input_line == ""
    
    token_len, matches = parse_token(input_line, pattern)
    if token_len > 0 and matches:
        return match_here(input_line[token_len:], pattern[len(get_token_pattern(pattern)):])
    
    return False

def get_token_pattern(pattern):
    """Get the actual pattern string for the current token"""
    if pattern.startswith('['):
        end = pattern.find(']')
        if end != -1:
            return pattern[:end+1]
    elif pattern.startswith('\\') and len(pattern) > 1:
        return pattern[:2]
    else:
        return pattern[0]

def parse_token(input_line, pattern):
    """Parse a single token and return (chars_consumed, matches)"""
    if not input_line:
        return 0, False
    
    if pattern.startswith('['):
        end = pattern.find(']')
        if end != -1:
            char_class = pattern[1:end]
            if char_class.startswith('^'):
                # Negative character class
                matches = input_line[0] not in char_class[1:]
            else:
                # Positive character class
                matches = input_line[0] in char_class
            return 1 if matches else 0, matches
    
    elif pattern.startswith('\\'):
        if len(pattern) > 1:
            if pattern[1] == 'd':
                return 1 if input_line[0].isdigit() else 0, input_line[0].isdigit()
            elif pattern[1] == 'w':
                return 1 if input_line[0].isalnum() or input_line[0] == '_' else 0, input_line[0].isalnum() or input_line[0] == '_'
    
    elif pattern[0] == '.':
        return 1, True
    
    else:
        return 1 if input_line[0] == pattern[0] else 0, input_line[0] == pattern[0]

def match_star(char, pattern, input_line):
    """Match zero or more occurrences of char followed by pattern"""
    if match_here(input_line, pattern):
        return True
    
    i = 0
    while i < len(input_line):
        token_len, matches = parse_token(input_line[i:], char)
        if not matches or token_len == 0:
            break
        
        if match_here(input_line[i + token_len:], pattern):
            return True
        
        i += 1
    
    return False


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    valid_args = ["-E"]
    if sys.argv[1] not in valid_args:
        print(f"Expected first argument to be of {valid_args}")
        exit(1)

    print(file=sys.stderr)

    if match_pattern(input_line, pattern):
        print("true")
        exit(0)
    else:
        print("false")
        exit(1)


if __name__ == "__main__":
    main()
