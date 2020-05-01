'''
 python3
 Author: Anthony Silva

 Description: In this program I will implement a simple phone book manager. It should be able to
    process the following types of user’s queries:

    ∙ add number name. It means that the user adds a person with name name and phone number number to
    the phone book. If there exists a user with such number already, then your manager has to overwrite
    the corresponding name.

    ∙ del number. It means that the manager should erase a person with number number from the phone book.
    If there is no such person, then it should just ignore the query.

    ∙ find number. It means that the user looks for a person with phone number number. The manager
    should reply with the appropriate name, or with string “not found" (without quotes) if there is no
    such person in the book.

 Input: There is a single integer 𝑁 in the first line — the number of queries. It’s followed by 𝑁 lines,
    each of them contains one query in the format described above.

 Output: Print the result of each find query — the name corresponding to the phone number or “not found"
    (without quotes) if there is no person in the phone book with such phone number. Output one result
    per line in the same order as the find queries are given in the input.


 Constraints: 1 ≤ 𝑁 ≤ 10 . All phone numbers consist of decimal digits, they don’t have leading zeros,
    and each of them has no more than 7 digits. All names are non-empty strings of latin letters,
    and each of them has length at most 15. It’s guaranteed that there is no person with name “not found".
'''

class Query:
	def __init__(self, query):
		self.type = query[0]
		self.number = int(query[1])
		if self.type == 'add':
			self.name = query[2]


def ReadQueries():
	n = int(input())
	return [Query(input().split()) for i in range(n)]


def WriteResponses(result):
	print('\n'.join(result))


def ProcessQueries(queries):
	result = []
	# Keep list of all existing (i.e. not deleted yet) contacts.
	contacts = {}
	for cur_query in queries:
		if cur_query.type == 'add':
			# if we already have contact with such number,
			# we should rewrite contact's name
			contacts[cur_query.number] = cur_query.name
		elif cur_query.type == 'del':
			if cur_query.number in contacts:
				del contacts[cur_query.number]
		else:
			response = 'not found' if cur_query.number not in contacts else contacts[cur_query.number]
			result.append(response)
	return result


if __name__ == '__main__':
	WriteResponses(ProcessQueries(ReadQueries()))