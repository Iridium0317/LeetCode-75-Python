import os
import json

# ==========================================
# 1. LeetCode 75 数据全集
# ==========================================
DATA = [
    ("Array / String", "01_Array_String", [
        ("1768_Merge_Strings_Alternately", "Easy"), 
        ("1071_GCD_of_Strings", "Easy"), 
        ("1431_Kids_With_Candies", "Easy"), 
        ("605_Can_Place_Flowers", "Easy"), 
        ("345_Reverse_Vowels_of_a_String", "Easy"), 
        ("151_Reverse_Words_in_a_String", "Medium"), 
        ("238_Product_of_Array_Except_Self", "Medium"), 
        ("334_Increasing_Triplet_Subsequence", "Medium"), 
        ("443_String_Compression", "Medium")
    ]),
    ("Two Pointers", "02_Two_Pointers", [
        ("283_Move_Zeroes", "Easy"), 
        ("392_Is_Subsequence", "Easy"), 
        ("11_Container_With_Most_Water", "Medium"), 
        ("1679_Max_Number_of_K_Sum_Pairs", "Medium")
    ]),
    ("Sliding Window", "03_Sliding_Window", [
        ("643_Maximum_Average_Subarray_I", "Easy"), 
        ("1456_Max_Vowels_in_Substring", "Medium"), 
        ("1004_Max_Consecutive_Ones_III", "Medium"), 
        ("1493_Longest_Subarray_of_1s_After_Deleting_One", "Medium")
    ]),
    ("Prefix Sum", "04_Prefix_Sum", [
        ("1732_Find_the_Highest_Altitude", "Easy"), 
        ("724_Find_Pivot_Index", "Easy")
    ]),
    ("Hash Map / Set", "05_Hash_Map_Set", [
        ("2215_Find_the_Difference_of_Two_Arrays", "Easy"), 
        ("1207_Unique_Number_of_Occurrences", "Easy"), 
        ("1657_Determine_if_Two_Strings_Are_Close", "Medium"), 
        ("2352_Equal_Row_and_Column_Pairs", "Medium")
    ]),
    ("Stack", "06_Stack", [
        ("2390_Removing_Stars_From_a_String", "Medium"), 
        ("735_Asteroid_Collision", "Medium"), 
        ("394_Decode_String", "Medium")
    ]),
    ("Queue", "07_Queue", [
        ("933_Number_of_Recent_Calls", "Easy"), 
        ("649_Dota2_Senate", "Medium")
    ]),
    ("Linked List", "08_Linked_List", [
        ("2095_Delete_the_Middle_Node_of_a_Linked_List", "Medium"), 
        ("328_Odd_Even_Linked_List", "Medium"), 
        ("206_Reverse_Linked_List", "Easy"), 
        ("2130_Maximum_Twin_Sum_of_a_Linked_List", "Medium")
    ]),
    ("Binary Tree - DFS", "09_Binary_Tree_DFS", [
        ("104_Maximum_Depth_of_Binary_Tree", "Easy"), 
        ("872_Leaf_Similar_Trees", "Easy"), 
        ("1448_Count_Good_Nodes_in_Binary_Tree", "Medium"), 
        ("437_Path_Sum_III", "Medium"), 
        ("1372_Longest_ZigZag_Path_in_a_Binary_Tree", "Medium"), 
        ("236_LCA_of_a_Binary_Tree", "Medium")
    ]),
    ("Binary Tree - BFS", "10_Binary_Tree_BFS", [
        ("199_Binary_Tree_Right_Side_View", "Medium"), 
        ("1161_Maximum_Level_Sum_of_a_Binary_Tree", "Medium")
    ]),
    ("Binary Search Tree", "11_Binary_Search_Tree", [
        ("700_Search_in_a_Binary_Search_Tree", "Easy"), 
        ("450_Delete_Node_in_a_BST", "Medium")
    ]),
    ("Graphs - DFS", "12_Graphs_DFS", [
        ("841_Keys_and_Rooms", "Medium"), 
        ("547_Number_of_Provinces", "Medium"), 
        ("1466_Reorder_Routes_to_Make_All_Paths_Lead_to_City_Zero", "Medium"), 
        ("399_Evaluate_Division", "Medium")
    ]),
    ("Graphs - BFS", "13_Graphs_BFS", [
        ("1926_Nearest_Exit_from_Entrance_in_Maze", "Medium"), 
        ("994_Rotting_Oranges", "Medium")
    ]),
    ("Heap / Priority Queue", "14_Heap_Priority_Queue", [
        ("215_Kth_Largest_Element_in_an_Array", "Medium"), 
        ("2336_Smallest_Number_in_Infinite_Set", "Medium"), 
        ("2542_Maximum_Subsequence_Score", "Medium"), 
        ("2462_Total_Cost_to_Hire_K_Workers", "Medium")
    ]),
    ("Binary Search", "15_Binary_Search", [
        ("374_Guess_Number_Higher_or_Lower", "Easy"), 
        ("2300_Successful_Pairs_of_Spells_and_Potions", "Medium"), 
        ("162_Find_Peak_Element", "Medium"), 
        ("875_Koko_Eating_Bananas", "Medium")
    ]),
    ("Backtracking", "16_Backtracking", [
        ("17_Letter_Combinations_of_a_Phone_Number", "Medium"), 
        ("216_Combination_Sum_III", "Medium")
    ]),
    ("DP - 1D", "17_DP_1D", [
        ("1137_N_th_Tribonacci_Number", "Easy"), 
        ("746_Min_Cost_Climbing_Stairs", "Easy"), 
        ("198_House_Robber", "Medium"), 
        ("790_Domino_and_Tromino_Tiling", "Medium")
    ]),
    ("DP - Multidimensional", "18_DP_Multidimensional", [
        ("62_Unique_Paths", "Medium"), 
        ("1143_Longest_Common_Subsequence", "Medium"), 
        ("714_Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee", "Medium"), 
        ("72_Edit_Distance", "Medium")
    ]),
    ("Bit Manipulation", "19_Bit_Manipulation", [
        ("338_Counting_Bits", "Easy"), 
        ("136_Single_Number", "Easy"), 
        ("1318_Minimum_Flips_to_Make_a_OR_b_Equal_to_c", "Medium")
    ]),
    ("Trie", "20_Trie", [
        ("208_Implement_Trie_Prefix_Tree", "Medium"), 
        ("1268_Search_Suggestions_System", "Medium")
    ]),
    ("Intervals", "21_Intervals", [
        ("435_Non_overlapping_Intervals", "Medium"), 
        ("452_Minimum_Number_of_Arrows_to_Burst_Balloons", "Medium")
    ]),
    ("Monotonic Stack", "22_Monotonic_Stack", [
        ("739_Daily_Temperatures", "Medium"), 
        ("901_Online_Stock_Span", "Medium")
    ])
]

# ==========================================
# 2. 智能 Notebook 解析 (Strict Mode)
# ==========================================
def analyze_notebook(filepath):
    if not os.path.exists(filepath):
        return "⬜", "⬜"

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        cells = data.get("cells", [])
        code_status = "⬜"
        note_status = "⬜"

        for cell in cells:
            source_lines = cell.get('source', [])
            source_text = "".join(source_lines).strip()
            
            # 1. 找代码 (Code)
            # 逻辑：长度 > 40 且不包含 pass。
            if cell['cell_type'] == 'code':
                if len(source_text) > 40 and "pass" not in source_text:
                    code_status = "✅"
            
            # 2. 找笔记 (Takeaways)
            # 逻辑：严格检测 [x] 或 [X]。
            # 我们删除了字数检测，因为默认模版太长了会被误判。
            if cell['cell_type'] == 'markdown':
                if "[x]" in source_text or "[X]" in source_text:
                    note_status = "✅"
        
        # 逻辑：有代码没笔记 -> 沙漏
        if code_status == "✅" and note_status == "⬜":
            note_status = "⏳"
            
        return code_status, note_status
        
    except Exception:
        return "⚠️", "⚠️"

# ==========================================
# 3. 生成 Markdown 内容
# ==========================================
header = """# LeetCode 75 - Python Notebooks

This repository contains my solutions and study notes for the LeetCode 75 study plan. 
Each problem is solved in its own **Jupyter Notebook (.ipynb)** to include detailed thought processes, complexity analysis, and diagrams.

## Tech Stack
- Language: Python 3
- Concepts: Data Structures & Algorithms

## Study Methodology: Spaced Repetition

- **Day 1 (Implementation)**: Focus on solving the problem and passing test cases.
- **Day 2 (Retrospection)**: Revisit the solution after 24 hours to write **Takeaways**, analyze complexity, and optimize code.

---

## Progress Tracker

| Category | Problem | Diff | Code | Takeaways |
| :--- | :--- | :--- | :---: | :---: |
"""

footer = """
---
*Created by Claire*
"""

content = header
total_solved = 0
DIFF_MAP = {"Easy": "Easy", "Medium": "Med", "Hard": "Hard"}

for category, folder, problems in DATA:
    is_first = True
    for prob_file, diff in problems:
        filepath = os.path.join(folder, f"{prob_file}.ipynb")
        c_stat, n_stat = analyze_notebook(filepath)
        if c_stat == "✅": total_solved += 1
        
        try:
            parts = prob_file.split("_")
            p_id = parts[0]
            p_name = " ".join(parts[1:])
            display_name = f"**{p_id}.** {p_name}"
        except:
            display_name = prob_file
            
        link = f"[{display_name}](./{folder}/{prob_file}.ipynb)"
        cat_col = f"**{category}**" if is_first else ""
        is_first = False
        short_diff = DIFF_MAP.get(diff, diff)
        
        content += f"| {cat_col} | {link} | {short_diff} | {c_stat} | {n_stat} |\n"

content += footer

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Strict Mode Update! Solved: {total_solved}")
