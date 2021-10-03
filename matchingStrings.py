# def matchingStrings(strings, queries):
#     count = 0
#     count_list = []
#     for q in queries:
#         count = 0
#         len_of_query = len(q)
#         for s in strings:
#             print(f'working on string {s} and query {q}')
#             len_of_string = len(s)
#             if len_of_string >= len_of_query:
#                 print(f'{len_of_string} is bigger or equal to {len_of_query}')
#                 tedad_barresi = len_of_string // len_of_query
#                 print(f'this string/query will be chcked {tedad_barresi} times ')
#                 for i in range(tedad_barresi):
#                     starting_idx = 0
#                     ending_idx = len_of_query
#                     if s[starting_idx:ending_idx] == q:
#                         print(f'{s[starting_idx:len_of_query]} from {s} is equal to {q}')
#                         count += 1
#                     else:
#                         print(f'no match found with {s[starting_idx:len_of_query]} and {q}')
#                     starting_idx += len_of_query
#                     ending_idx += len_of_query
#
#             else:
#                 print(
#                     f'{len_of_string} which is len of {s} is not bigger or equal to {len_of_query} which is the len of {q}')
#         print('\n\n')
#
#         count_list.append(count)
#
#     print(count_list)
#
#
# matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
#
#
# def matchingStrings2(strings, queries):
#     idx = int
#     # ending_loop_idx - starting_loop_idx = 2
#     # count_of_checked_idx_in_loop = when hits 2 the loop has ended
#     #
#
#
# matchingStrings2(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
#
# import re
#
#
# def matchStrings3(strings, queries):
#     count = 0
#     count_in_loop = 0
#     for q in queries:
#         for s in strings:
#             count_in_loop = len(re.findall(q, s))
#             count += count_in_loop
#             print(f'found {count_in_loop} for {q} x {s}')
#     return print(count)
#
# matchStrings3(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
#
#
#
#


def matchStrings4(strings, queries):
    list_of_count = []
    for q in queries:
        count_for_q = 0
        for s in strings:
            if q == s:
                count_for_q += 1
            else:
                pass
        list_of_count.append(count_for_q)

    return print(list_of_count)


matchStrings4(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])