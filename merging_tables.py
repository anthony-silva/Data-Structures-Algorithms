'''
 Python3
 Author: Anthony Silva

 Objective: In this program, the goal is to simulate a sequence of merge operations with tables
    in a database. There are 𝑛 tables stored in some database. The tables are numbered from
    1 to 𝑛. All tables share the same set of columns. Each table contains either several rows
    with real data or a symbolic link to another table. Initially, all tables contain data, and
    𝑖-th table has 𝑟𝑖 rows. You need to perform 𝑚 of the following operations:

        1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖. Traverse the path of symbolic links to get to the data.
        That is, while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖 contains a symbolic link instead of real data do
        𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖)

        2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒_𝑖 and traverse the path of symbolic links from it in the
        same manner as for 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖.

        3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒_𝑖 are the numbers of two tables with real data. If 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖 != 𝑠𝑜𝑢𝑟𝑐𝑒_𝑖,
        copy all the rows from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖, then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒_𝑖 and instead
        of real data put a symbolic link to 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖 into it.

        4. Print the maximum size among all 𝑛 tables (recall that size is the number of rows in the table).
        If the table contains only a symbolic link, its size is considered to be 0.

 Input: The first line of the input contains two integers 𝑛 and 𝑚 — the number of tables
    in the database and the number of merge queries to perform, respectively.
    The second line of the input contains 𝑛 integers 𝑟𝑖 — the number of rows in the 𝑖-th table.
    Then follow 𝑚 lines describing merge queries. Each of them contains two integers 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑖
    and 𝑠𝑜𝑢𝑟𝑐𝑒_𝑖 — the numbers of the tables to merge.

 Output: For each query print a line containing a single integer — the maximum of the sizes of all
    tables (in terms of the number of rows) after the corresponding operation.
'''

def GetParent(table):
    global parent
    parents_to_update = [] # find parent and compress path

    root = table # find root
    while root != parent[root]:
        parents_to_update.append(parent[root])
        root = parent[root]

    # compress path
    for i in parents_to_update:
        parent[i] = root

    return root


def Merge(destination, source):
    global solution
    real_destination, real_source = GetParent(destination), GetParent(source)

    if real_destination == real_source:
        return False

    if rank[real_destination] < rank[real_source]:
        parent[real_destination] = real_source
        lines[real_source] += lines[real_destination]
        solution = max(solution, lines[real_source])
    else:
        parent[real_source] = real_destination
        lines[real_destination] += lines[real_source]
        solution = max(solution, lines[real_destination])
        if rank[real_destination] == rank[real_source]:
            rank[real_destination] += 1

if __name__=="__main__":
    n, m = map(int, input().split())
    lines = [int(x) for x in input().split()]
    rank = [1] * n
    parent = [i for i in range(0, n)]
    solution = max(lines)
    solutions = [0] * m

    for i in range(m):
        destination, source = map(int, input().split())
        Merge(destination-1, source-1)
        solutions[i] = solution

    for ans in solutions:
        print(ans)