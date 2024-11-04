# Input
num_transactions = int(input("Enter the number of transactions: "))
transactions = [set(map(int, input(f"Items in transaction {i + 1}: ").split())) for i in range(num_transactions)]
min_support = float(input("Enter minimum support (in %): "))
min_confidence = float(input("Enter minimum confidence (in %): "))

# Support calculation
def get_support(itemset):
    """Calculates the support percentage for a given itemset."""
    return sum(1 for t in transactions if itemset <= t) / len(transactions) * 100

# Subset generation for antecedents in association rules
def get_non_empty_subsets(itemset):
    """Generates all non-empty subsets of an itemset, except the full set itself."""
    items = list(itemset)
    subsets = []
    for i in range(1, len(items)):
        subsets.extend([frozenset(items[j] for j in range(len(items)) if k & (1 << j)) for k in range(1 << len(items)) if bin(k).count('1') == i])
    return subsets

# Frequent itemsets
itemsets, frequent_itemsets, k = [{frozenset([item]) for t in transactions for item in t}], [], 1
while itemsets[-1]:
    current = {i for i in itemsets[-1] if get_support(i) >= min_support}
    if not current: break
    frequent_itemsets.append(current)
    itemsets.append({i | j for i in current for j in current if len(i | j) == k + 1})
    k += 1

# Output frequent itemsets
print("\nFrequent Itemsets:")
for i, itemset in enumerate(frequent_itemsets, 1):
    print(f"{i}-itemsets:", [list(x) for x in itemset])

# Generate association rules with confidence above min_confidence
print("\nAssociation Rules:")
for itemset_group in frequent_itemsets[1:]:  # Start from 2-itemsets
    for itemset in itemset_group:
        for antecedent in get_non_empty_subsets(itemset):
            consequent = itemset - antecedent
            if consequent and get_support(antecedent) > 0:
                confidence = get_support(itemset) / get_support(antecedent) * 100
                # Only print rules with confidence above min_confidence
                if confidence >= min_confidence:
                    print(f"{list(antecedent)} -> {list(consequent)}, Confidence = {confidence:.2f}%")
