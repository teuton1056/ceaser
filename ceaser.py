#!/usr/bin/env python3

# ceaser.py version 0.1.0- A simple Ceaser Cipher solver, encoder, and decoder
# written to provide basic functionality for solving Ceaser Ciphers
# since it seems like it just kept coming up (also it provided a nice
# chance to get to know the argparse module a bit better).
# Written by: Jordan Furutani
# Tested using Python 3.11.3

import argparse
from io import TextIOWrapper
import sys

from click import File

def builtin_word_list() -> set[str]:
    # a list of the 1000 most common words in the English language
    wordlist =  set(['the', 'of', 'and', 'to', 'a', 'in', 'for', 'is', 'on', 'that', 'by', 'this', 'with', 'i', 'you', 'it', 'not', 'or', 'be', 'are', 'from', 'at', 'as', 'your', 'all', 'have', 'new', 'more', 'an', 'was', 'we', 'will', 'home', 'can', 'us', 'about', 'if', 'page', 'my', 'has', 'search', 'free', 'but', 'our', 'one', 'other', 'do', 'no', 'information', 'time', 'they', 'site', 'he', 'up', 'may', 'what', 'which', 'their', 'news', 'out', 'use', 'any', 'there', 'see', 'only', 'so', 'his', 'when', 'contact', 'here', 'business', 'who', 'web', 'also', 'now', 'help', 'get', 'pm', 'view', 'online', 'c', 'e', 'first', 'am', 'been', 'would', 'how', 'were', 'me', 's', 'services', 'some', 'these', 'click', 'its', 'like', 'service', 'x', 'than', 'find', 'price', 'date', 'back', 'top', 'people', 'had', 'list', 'name', 'just', 'over', 'state', 'year', 'day', 'into', 'email', 'two', 'health', 'n', 'world', 're', 'next', 'used', 'go', 'b', 'work', 'last', 'most', 'products', 'music', 'buy', 'data', 'make', 'them', 'should', 'product', 'system', 'post', 'her', 'city', 't', 'add', 'policy', 'number', 'such', 'please', 'available', 'copyright', 'support', 'message', 'after', 'best', 'software', 'then', 'jan', 'good', 'video', 'well', 'd', 'where', 'info', 'rights', 'public', 'books', 'high', 'school', 'through', 'm', 'each', 'links', 'she', 'review', 'years', 'order', 'very', 'privacy', 'book', 'items', 'company', 'r', 'read', 'group', 'sex', 'need', 'many', 'user', 'said', 'de', 'does', 'set', 'under', 'general', 'research', 'university', 'january', 'mail', 'full', 'map', 'reviews', 'program', 'life', 'know', 'games', 'way', 'days', 'management', 'p', 'part', 'could', 'great', 'united', 'hotel', 'real', 'f', 'item', 'international', 'center', 'ebay', 'must', 'store', 'travel', 'comments', 'made', 'development', 'report', 'off', 'member', 'details', 'line', 'terms', 'before', 'hotels', 'did', 'send', 'right', 'type', 'because', 'local', 'those', 'using', 'results', 'office', 'education', 'national', 'car', 'design', 'take', 'posted', 'internet', 'address', 'community', 'within', 'states', 'area', 'want', 'phone', 'dvd', 'shipping', 'reserved', 'subject', 'between', 'forum', 'family', 'l', 'long', 'based', 'w', 'code', 'show', 'o', 'even', 'black', 'check', 'special', 'prices', 'website', 'index', 'being', 'women', 'much', 'sign', 'file', 'link', 'open', 'today', 'technology', 'south', 'case', 'project', 'same', 'pages', 'uk', 'version', 'section', 'own', 'found', 'sports', 'house', 'related', 'security', 'both', 'g', 'county', 'american', 'photo', 'game', 'members', 'power', 'while', 'care', 'network', 'down', 'computer', 'systems', 'three', 'total', 'place', 'end', 'following', 'download', 'h', 'him', 'without', 'per', 'access', 'think', 'north', 'resources', 'current', 'posts', 'big', 'media', 'law', 'control', 'water', 'history', 'pictures', 'size', 'art', 'personal', 'since', 'including', 'guide', 'shop', 'directory', 'board', 'location', 'change', 'white', 'text', 'small', 'rating', 'rate', 'government', 'children', 'during', 'usa', 'return', 'students', 'v', 'shopping', 'account', 'times', 'sites', 'level', 'digital', 'profile', 'previous', 'form', 'events', 'love', 'old', 'john', 'main', 'call', 'hours', 'image', 'department', 'title', 'description', 'non', 'k', 'y', 'insurance', 'another', 'why', 'shall', 'property', 'class', 'cd', 'still', 'money', 'quality', 'every', 'listing', 'content', 'country', 'private', 'little', 'visit', 'save', 'tools', 'low', 'reply', 'customer', 'december', 'compare', 'movies', 'include', 'college', 'value', 'article', 'york', 'man', 'card', 'jobs', 'provide', 'j', 'food', 'source', 'author', 'different', 'press', 'u', 'learn', 'sale', 'around', 'print', 'course', 'job', 'canada', 'process', 'teen', 'room', 'stock', 'training', 'too', 'credit', 'point', 'join', 'science', 'men', 'categories', 'advanced', 'west', 'sales', 'look', 'english', 'left', 'team', 'estate', 'box', 'conditions', 'select', 'windows', 'photos', 'gay', 'thread', 'week', 'category', 'note', 'live', 'large', 'gallery', 'table', 'register', 'however', 'june', 'october', 'november', 'market', 'library', 'really', 'action', 'start', 'series', 'model', 'features', 'air', 'industry', 'plan', 'human', 'provided', 'tv', 'yes', 'required', 'second', 'hot', 'accessories', 'cost', 'movie', 'forums', 'march', 'la', 'september', 'better', 'say', 'questions', 'july', 'yahoo', 'going', 'medical', 'test', 'friend', 'come', 'dec', 'server', 'pc', 'study', 'application', 'cart', 'staff', 'articles', 'san', 'feedback', 'again', 'play', 'looking', 'issues', 'april', 'never', 'users', 'complete', 'street', 'topic', 'comment', 'financial', 'things', 'working', 'against', 'standard', 'tax', 'person', 'below', 'mobile', 'less', 'got', 'blog', 'party', 'payment', 'equipment', 'login', 'student', 'let', 'programs', 'offers', 'legal', 'above', 'recent', 'park', 'stores', 'side', 'act', 'problem', 'red', 'give', 'memory', 'performance', 'social', 'q', 'august', 'quote', 'language', 'story', 'sell', 'options', 'experience', 'rates', 'create', 'key', 'body', 'young', 'america', 'important', 'field', 'few', 'east', 'paper', 'single', 'ii', 'age', 'activities', 'club', 'example', 'girls', 'additional', 'password', 'z', 'latest', 'something', 'road', 'gift', 'question', 'changes', 'night', 'ca', 'hard', 'texas', 'oct', 'pay', 'four', 'poker', 'status', 'browse', 'issue', 'range', 'building', 'seller', 'court', 'february', 'always', 'result', 'audio', 'light', 'write', 'war', 'nov', 'offer', 'blue', 'groups', 'al', 'easy', 'given', 'files', 'event', 'release', 'analysis', 'request', 'fax', 'china', 'making', 'picture', 'needs', 'possible', 'might', 'professional', 'yet', 'month', 'major', 'star', 'areas', 'future', 'space', 'committee', 'hand', 'sun', 'cards', 'problems', 'london', 'washington', 'meeting', 'rss', 'become', 'interest', 'id', 'child', 'keep', 'enter', 'california', 'porn', 'share', 'similar', 'garden', 'schools', 'million', 'added', 'reference', 'companies', 'listed', 'baby', 'learning', 'energy', 'run', 'delivery', 'net', 'popular', 'term', 'film', 'stories', 'put', 'computers', 'journal', 'reports', 'co', 'try', 'welcome', 'central', 'images', 'president', 'notice', 'god', 'original', 'head', 'radio', 'until', 'cell', 'color', 'self', 'council', 'away', 'includes', 'track', 'australia', 'discussion', 'archive', 'once', 'others', 'entertainment', 'agreement', 'format', 'least', 'society', 'months', 'log', 'safety', 'friends', 'sure', 'faq', 'trade', 'edition', 'cars', 'messages', 'marketing', 'tell', 'further', 'updated', 'association', 'able', 'having', 'provides', 'david', 'fun', 'already', 'green', 'studies', 'close', 'common', 'drive', 'specific', 'several', 'gold', 'feb', 'living', 'sep', 'collection', 'called', 'short', 'arts', 'lot', 'ask', 'display', 'limited', 'powered', 'solutions', 'means', 'director', 'daily', 'beach', 'past', 'natural', 'whether', 'due', 'et', 'electronics', 'five', 'upon', 'period', 'planning', 'database', 'says', 'official', 'weather', 'mar', 'land', 'average', 'done', 'technical', 'window', 'france', 'pro', 'region', 'island', 'record', 'direct', 'microsoft', 'conference', 'environment', 'records', 'st', 'district', 'calendar', 'costs', 'style', 'url', 'front', 'statement', 'update', 'parts', 'aug', 'ever', 'downloads', 'early', 'miles', 'sound', 'resource', 'present', 'applications', 'either', 'ago', 'document', 'word', 'works', 'material', 'bill', 'apr', 'written', 'talk', 'federal', 'hosting', 'rules', 'final', 'adult', 'tickets', 'thing', 'centre', 'requirements', 'via', 'cheap', 'nude', 'kids', 'finance', 'true', 'minutes', 'else', 'mark', 'third', 'rock', 'gifts', 'europe', 'reading', 'topics', 'bad', 'individual', 'tips', 'plus', 'auto', 'cover', 'usually', 'edit', 'together', 'videos', 'percent', 'fast', 'function', 'fact', 'unit', 'getting', 'global', 'tech', 'meet', 'far', 'economic', 'en', 'player', 'projects', 'lyrics', 'often', 'subscribe', 'submit', 'germany', 'amount', 'watch', 'included', 'feel', 'though', 'bank', 'risk', 'thanks', 'everything', 'deals', 'various', 'words', 'linux', 'jul', 'production', 'commercial', 'james', 'weight', 'town', 'heart', 'advertising', 'received', 'choose', 'treatment', 'newsletter', 'archives', 'points', 'knowledge', 'magazine', 'error', 'camera', 'jun', 'girl', 'currently', 'construction', 'toys', 'registered', 'clear', 'golf', 'receive', 'domain', 'methods', 'chapter', 'makes', 'protection', 'policies', 'loan', 'wide', 'beauty', 'manager', 'india', 'position', 'taken', 'sort', 'listings', 'models', 'michael', 'known', 'half', 'cases', 'step', 'engineering', 'florida', 'simple', 'quick', 'none', 'wireless', 'license', 'paul', 'friday', 'lake', 'whole', 'annual', 'published', 'later', 'basic', 'sony', 'shows', 'corporate', 'google', 'church', 'method', 'purchase', 'customers', 'active', 'response', 'practice', 'hardware', 'figure', 'materials', 'fire', 'holiday', 'chat', 'enough', 'designed', 'along', 'among', 'death', 'writing', 'speed', 'html', 'countries', 'loss', 'face', 'brand', 'discount', 'higher', 'effects', 'created', 'remember', 'standards', 'oil', 'bit', 'yellow', 'political', 'increase', 'advertise', 'kingdom', 'base', 'near', 'environmental', 'thought', 'stuff', 'french', 'storage', 'oh', 'japan', 'doing', 'loans', 'shoes'])
    wordlist.add('hello')
    return wordlist


def ceaser_shift(text: str, shift: int) -> str:
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr(ascii_offset + (ord(char) - ascii_offset + shift) % 26)
        else:
            result += char
    return result


def ceaser_unshift(text: str, shift: int) -> str:
    return ceaser_shift(text, -shift)


def ceaser_brute_force(text: str) -> dict[int, str]:
    solutions = {}
    for shift in range(26):
        solutions[shift] = ceaser_unshift(text, shift)
    return solutions


def _grade_solution(text: str, word_list: set[str]) -> int:
    words = text.split()
    return sum([1 for word in words if word in word_list])


def _grade_solution_no_spaces(text: str, word_list: set[str]) -> int:
    grade = 0
    for word in word_list:
        if word in text:
            grade += 1
    return grade


def ceaser_solver(text: str ,word_list: set[str], hint="") -> str | None:
    solutions = ceaser_brute_force(text)
    graded_solutions: dict[int, int] = {}
    best = 0
    if hint:
        solutions_with_hint = {}
        for i in range(26):
            if hint in solutions[i]:
                solutions_with_hint[i] = solutions[i]
        if solutions_with_hint:
            solutions = solutions_with_hint
    for i in solutions.keys():
        graded_solutions[i] = _grade_solution(solutions[i], word_list)
        if graded_solutions[i] > best:
            best = i
    if best == 0:
        for i in solutions.keys():
            graded_solutions[i] = _grade_solution_no_spaces(solutions[i], word_list)
            if graded_solutions[i] > best:
                best = i
    if best == 0:
        return None
    return solutions[best]


def output_solution(text: str, file: TextIOWrapper) -> None:
    if not file:
        print(text)
    else:
        file.write(text)
        file.close()


def main() -> int:
    builtin_word_list()
    parser = argparse.ArgumentParser(description='Ceaser Cipher Solver', exit_on_error=False)
    input_group = parser.add_argument_group('Input Options', description='The input text to decode, if not provided, will read from stdin')
    input_options_group = input_group.add_mutually_exclusive_group(required=False)
    input_options_group.add_argument('-i','--input-file', type=argparse.FileType('r'), help='the file containing the cipher text')
    input_options_group.add_argument('-c','--cipher_text', type=str, help='the cipher text to decode')

    output_options_group = parser.add_argument_group('Output Options', description='The output options, if not used will print to stdout')
    output_options_group.add_argument('-o','--output-file', type=argparse.FileType('w'), help='the file to write the output to')

    operation_group = parser.add_argument_group('Operation Options', description='The operation to perform on the input text')
    operation_exclusive_group = operation_group.add_mutually_exclusive_group(required=True)
    operation_exclusive_group.add_argument('-e', '--encode', type=int, help='encode the text, requires a shift value')
    operation_exclusive_group.add_argument('-d', '--decode', type=int, help='decode the text, requires a shift value')
    operation_exclusive_group.add_argument('-s', '--solve', action='store_true', help='attempt to solve the cipher')
    operation_exclusive_group.add_argument('-b', '--brute_force', action='store_true', help='brute force the solution')

    solution_assists_group = parser.add_argument_group('Solution Assists', description='Options to assist in solving the cipher, only used with -s')
    solution_assists_group.add_argument('-w','--word_list', type=argparse.FileType('r'), help='the word list to use when solving the cipher')
    solution_assists_group.add_argument('-H','--hint', type=str, help='a string which is known to appear in the plain text')

    brute_force_group = parser.add_argument_group('Brute Force Options', description='Options to help when brute forcing the solution, only used with -b')
    brute_force_group.add_argument('-bl','--brute_force_limit', type=int, help='the length of each solution to print, useful for very long strings')

    # basic options
    parser.add_argument('-v','--verbose', action='store_true', help='verbose output')
    parser.add_argument('-q','--quiet', action='store_true', help='quiet output')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.1.0')

    args = parser.parse_args()

    if (args.word_list or args.hint) and not args.solve:
        parser.error('word_list and hint options are only valid with the -s option')
    elif args.brute_force_limit and not args.brute_force:
        parser.error('brute_force_limit is only valid with the -b option')

    if args.input_file:
        args.cipher_text = args.input_file.read()
    if not args.cipher_text:
        args.cipher_text = sys.stdin.read()

    if args.encode:
        if args.verbose:
            print(f'Encoding {args.cipher_text} with shift {args.encode}')
        output_solution(ceaser_shift(args.cipher_text, args.encode), args.output_file)
        #print(ceaser_shift(args.cipher_text, args.encode))
        return 0
    elif args.decode:
        if args.verbose:
            print(f'Decoding {args.cipher_text} with shift {args.decode}')
        output_solution(ceaser_unshift(args.cipher_text, args.decode), args.output_file)
        return 0
    elif args.brute_force:
        if args.verbose:
            print(f'Brute forcing {args.cipher_text}')
        solutions = ceaser_brute_force(args.cipher_text)
        if args.verbose and args.brute_force_limit:
            print(f"Printing only the first {args.brute_force_limit} characters of each solution")
        for shift, solution in solutions.items():
            if args.brute_force_limit:
                if shift < 10:
                    print(f'Shift: {shift}  Solution: {solution[:args.brute_force_limit]}')
                else:
                    print(f'Shift: {shift}  Solution: {solution[:args.brute_force_limit]}')
            else:
                if shift < 10:
                    print(f'Shift: {shift}  Solution: {solution}')
                else:
                    print(f'Shift: {shift} Solution: {solution}')
        return 0
    elif args.solve:
        if args.word_list:
            word_list: set[str] = set([word.strip() for word in args.word_list.readlines()])
        else:
            if args.verbose:
                print('No word list provided (-w), a short builtin word-list will be used, try using the -b option for all possible solutions')
            word_list = builtin_word_list()
        if ' ' not in args.cipher_text and len(args.cipher_text) > 10 and not args.quiet:
            print('No spaces detected in the cipher text, performance most likely be poor, consider using the -b option for all possible solutions')

        solution = ceaser_solver(args.cipher_text, word_list, hint=args.hint)
        if solution:
            output_solution(solution, args.output_file)
        else:
            print('No solution found')
        return 0
    else:
        print("No operation specified") # This should be caught by the argparse module
    return 3

if __name__ == '__main__':
    exit(main())
