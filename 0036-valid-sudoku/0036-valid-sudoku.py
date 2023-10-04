import collections

class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Divide the problem into 3 sub-problems
        
        # Track rows
        # Track columns
        # Track sub-boxes

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or 
                    board[i][j] in squares[(i // 3), (j // 3)]):
                        return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3), (j // 3)].add(board[i][j])
                
        
        return True

        
        # Let's work on tracking the rows
        # num_rows = len(board)
        # print("Number of rows: ", num_rows)
        
        # for i in range(len(board)):
        #     rows_set = ()
        #     for j in range(len(boards)):
        #         if board[i][j] != "." and int(board[i][j]) >= 1 and int(board[i][j]) <= 9:
        #             if board[i][j] not in rows_set:
        #                 rows_set.add(board[i][j])
        #             else:
        #                 return False
        
        # # Let's work on tracking the columns
        # for i in range(len(board)):
        #     cols_set = ()
        #     for j in range(len(boards)):
        #         if board[j][i] != "." and int(board[j][i]) >= 1 and int(board[j][i]) <= 9:
        #             if board[j][i] not in cols_set:
        #                 cols_set.add(board[j][i])
        #             else:
        #                 return False

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         # Dictionary 1: Track rows
#         # Dictionary 2: Track columns
#         # Dictionary 3: Track sub-boxes

#         num_rows = len(board)
#         num_cols = len(board[0])

#         # 1
#         for i in range(num_rows):
#             temp_set = set()
#             for j in range(num_cols):
#                 if board[i][j] != "." and int(board[i][j]) >=1 and int(board[i][j]) <= 9:
#                     c1 = len(temp_set)
#                     temp_set.add(board[i][j])
#                     c2 = len(temp_set)
#                     if c1 == c2:
#                         return False
        
#         # 2
#         for j in range(num_cols):
#             temp_set = set()
#             for i in range(num_rows):
#                 if board[i][j] != "." and int(board[i][j]) >=1 and int(board[i][j]) <= 9:
#                     c1 = len(temp_set)
#                     temp_set.add(board[i][j])
#                     c2 = len(temp_set)
#                     if c1 == c2:
#                         return False
        
#         # 3
#         keys = [
#             ["00", "22"], ["03", "25"], ["06", "28"],
#             ["30", "52"], ["33", "55"], ["36", "58"],
#             ["60", "82"], ["63", "85"], ["66", "88"]
#         ]

#         for key in keys:

#             i_start = int(key[0][0])
#             i_stop = int(key[1][0])
#             j_start = int(key[0][1])
#             j_stop = int(key[1][1])

#             temp_set = set()

#             for i in range(i_start, i_stop+1):
#                 for j in range(j_start, j_stop+1):
#                     if board[i][j] != "." and int(board[i][j]) >=1 and int(board[i][j]) <= 9:
#                         c1 = len(temp_set)
#                         temp_set.add(board[i][j])
#                         c2 = len(temp_set)
#                         if c1 == c2:
#                             return False

#         return True
        
        

