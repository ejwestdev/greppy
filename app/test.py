import sys

LITERAL = 0
DIGIT = 1
ALNUM = 2
POS_CHAR_GROUP = 3
NEG_CHAR_GROUP = 4

def match_next(input_line, token, pattern):
    if token == DIGIT:
        if input_line[0].isdigit():
            return input_line[1:]
        else:
            return False
    if token == ALNUM:
        if input_line[0].isalnum():
            return input_line[1:]
        else:
            return False
    if token == POS_CHAR_GROUP:
        if input_line[0] in pattern:
            return input_line[1:]
        else:
            return False
    if token == NEG_CHAR_GROUP:
        if input_line[0] not in pattern:
            return input_line[1:]
        else:
            return False
    if token == LITERAL:
        if input_line.startswith(pattern):
            return input_line[len(pattern):]
        else:
            return False

def determine_token(pattern):
    if len(pattern) >= 2 and pattern[:2] == "\\d":        
        return DIGIT, pattern[2:]
    if len(pattern) > 2 and pattern[:2] == "\\w":
        return ALNUM, pattern[2:]
    if len(pattern) >= 2 and pattern[:2] == "[^":
        return NEG_CHAR_GROUP, pattern[2:]
    elif pattern[0] == "[":
        return POS_CHAR_GROUP, pattern[pattern.index("]") + 1:]
    else:
        return LITERAL, pattern[1:]
            
def match_pattern(input_line, pattern, token_satisfied):
    while input_line:
        if pattern == "":
            return True
        next_token, remaining_pattern = determine_token(pattern)
        
        if remaining_pattern == "" and input_line == "" and token_satisfied:
            return True
        result = match_next(input_line, next_token, pattern)
        if not result:
            input_line = input_line[1:]
        else:
            input_line = result
            token_satisfied = True
            pattern = remaining_pattern
    return pattern