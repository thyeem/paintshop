# Note: here assumed that ONLY VALID DATA will be given.
# In order to focus on the algorithm itself, I skipped all validations of
# input files and command-line arguments.

def parse_input(lines):
    """parse the given file lines and sort it as a pre-process
    """
    lines = lines[::-1]
    data = []
    for _ in range(int(lines.pop())):
        num_colors = int(lines.pop())
        num_customers = int(lines.pop())
        customers = []
        for _ in range(num_customers):
            pairs = [ int(x) for x in lines.pop().split() ]
            customer = zip(pairs[1::2], pairs[2::2])
            customers.append(sort_customer(customer))
        data.append((num_colors, sort_customers(customers)))
    return data

def sort_customer(customer):
    """sort 'smaller color index' and 'glossy' first 
    among (X: color, Y: glossy | matte) pairs that a customer has.
    """
    return sorted(sorted(customer, key=lambda x: x[0]), key=lambda x: x[1])

def sort_customers(customers):
    """sort 'smaller length of color set' first among all the customers
    """
    return sorted(customers, key=len)

def traverse_trie(trie, track, depth, num_customers, num_colors):
    if depth == num_customers: return track 
    for color, matte in trie[depth]:
        if (color, matte ^ 1) in track: continue
        new_track = set(track)
        if not (color, matte) in track: new_track.add((color, matte))
        if len(new_track) > num_colors: continue
        result = traverse_trie(trie, new_track, depth+1, num_customers, num_colors)
        if result: return result
    return None

def evalute_result(result, nth, num_colors):
    output = f'Case #{nth}: '
    if not result:
        output += 'IMPOSSIBLE'
    else:
        matte = [ '1' if (i, 1) in result else '0' for i in range(1, num_colors+1) ]
        output += ' '.join(matte)
    return output

def solve_each_case(nth, case):
    num_colors, trie = case
    result = traverse_trie(trie, set(), 0, len(trie), num_colors)
    return evalute_result(result, nth, num_colors)

def run(filename):
    with open(filename, 'r') as f:
        data = parse_input([ line.strip() for line in f if line.strip() ])
        return [ solve_each_case(i+1, case) for i, case in enumerate(data) ]


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(5000)
    print('\n'.join(run(sys.argv[1])))

