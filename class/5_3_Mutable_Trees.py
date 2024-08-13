class Tree:
    def __init__(self, lable, branches=[]):
        self.lable = lable
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree{0}{1}'.format(self.lable, branch_str)
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
    
def count_leaves(t):
    if t.is_leaf():
        return 1
    else:
        branch_counts = 0
        for b in t.branches:
            branch_counts += count_leaves(b)
        return branch_counts
    
def prune_even(t):
    """Mutate the tree t such that all nodes containing even values are removed."""
    if is_even(t.lable):
        return
    new_branches = []
    for b in t.branches:
        if not is_even(b.label):
            prune_even(b)
            new_branches.append(b)
    t.branches = new_branches

def is_even(n):
    return n % 2 == 0

def largest_of_group(t):
    largest_labels = [t.label]
    for b in t.branches:
        largest_of_group(b)
        largest_labels.append(b.label)
    t.label = max(largest_labels)

def largest_of_group2(t):
    for b in t.branches:
        largest_of_group2(b)
    t.label = max([t] + t.branches, key=lambda n: n.label).label

def keep_k_largest(t, k):
    n = len(t.branches)
    counter = k
    while counter > n:
        smallest = min(t.branches, key=lambda n: n.label)
        t.branches.remove(smallest)
        counter - 1
    for b in t.branches:
        keep_k_largest(b, k)

def search_tree(t, x):
    if t.label == x:
        return True
    for b in t.branches:
        found = search_tree(b, x)
        if found:
            return True
    return False