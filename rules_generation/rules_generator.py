from itertools import product
import pandas as pd

LINGUISTIC_VARS = {
    "null_links": ["Low", "Moderate", "High"],
    "ext_css": ["Very Few", "Few", "Normal"],
    "domain_reg": ["Short", "Medium", "Long"],
    "traffic": ["Very Low", "Low", "Moderate", "High"],
    "page_rank": ["Popular", "Moderately Known", "Not Very Known"],
}


def generate_all_rules():
    input_vars = ["null_links", "ext_css", "domain_reg", "traffic", "page_rank"]
    combinations = product(*(LINGUISTIC_VARS[var] for var in input_vars))

    rules = []
    for combo in combinations:
        rule = dict(zip(input_vars, combo))
        rules.append(rule)

    return rules


def is_rule_covered(specific_rule, general_rule):
    for key, value in general_rule.items():
        if value != "*" and specific_rule[key] != value:
            return False
    return True


def apply_general_rules(rules, general_rules):
    remaining_rules = []
    covered_indices = set()

    for i, rule in enumerate(rules):
        for gen_rule in general_rules:
            if is_rule_covered(rule, gen_rule):
                covered_indices.add(i)
                break

    for i, rule in enumerate(rules):
        if i not in covered_indices:
            remaining_rules.append(rule)

    return remaining_rules + general_rules


if __name__ == "__main__":
    all_rules = generate_all_rules()
    df_original = pd.DataFrame(all_rules)
    print(f"Total number of initial rules: {len(all_rules)}")

    general_rules = [
        {
            "null_links": "High",
            "ext_css": "*",
            "domain_reg": "*",
            "traffic": "*",
            "page_rank": "*",
        },
        {
            "null_links": "*",
            "ext_css": "*",
            "domain_reg": "*",
            "traffic": "*",
            "page_rank": "Popular",
        },
        {
            "null_links": "Low",
            "ext_css": "*",
            "domain_reg": "*",
            "traffic": "*",
            "page_rank": "*",
        },
        {
            "null_links": "*",
            "ext_css": "Very Few",
            "domain_reg": "*",
            "traffic": "*",
            "page_rank": "*",
        },
        {
            "null_links": "*",
            "ext_css": "Few",
            "domain_reg": "*",
            "traffic": "High",
            "page_rank": "*",
        },
        {
            "null_links": "*",
            "ext_css": "*",
            "domain_reg": "Long",
            "traffic": "*",
            "page_rank": "*",
        },
    ]

    reduced_rules = apply_general_rules(all_rules, general_rules)
    df_reduced = pd.DataFrame(reduced_rules)

    print(f"Number of rules after applying general rules: {len(reduced_rules)}")
    print("\nGeneral rules applied:")
    for rule in general_rules:
        print(rule)

    df_original.to_csv("all_rules.csv", index=False)
    df_reduced.to_csv("reduced_rules.csv", index=False)
