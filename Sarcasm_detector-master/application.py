# from app import app
# app.run()
# from app import evaluate
import csv

def is_fake(str_fake):
    if str_fake == "FAKE":
        return 1
    return 0

def getstuff(filename):
    csvfile = open(filename, "rb")
    datareader = csv.reader(csvfile)
    resultCSVFile = open('sarcasm-result.csv', 'rb')
    resultreader = csv.reader(resultCSVFile)
    # spamwriter = csv.writer(resultCSVFile, delimiter=' ',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)

    title_index = 1
    body_index = 2
    answer_index = 3
    hits_and = 0
    hits_or = 0
    iterations = 0
    for row in datareader:
        row_result = next(resultreader)  # gets the first line
        if row[0] == '':
            print "what"
            continue

        iterations+=1
        # title_score = evaluate.tweetscore(row[title_index])
        # body_score = evaluate.tweetscore(row[body_index])
        title_score = float(row_result[0])
        body_score = float(row_result[1])
        print str(title_score) + " " + str(body_score)
        answer_score = is_fake(row[answer_index])

    # Write results to csv
    # spamwriter.writerow([str(title_score), str(body_score)])

        # if title_score > 0:
        #     title_score = 1
        # else:
        #     title_score = 0
        #
        # if body_score > 0:
        #     body_score = 1
        # else:
        #     body_score = 0
        if ((title_score * 1 / 4 + body_score * 3 / 4 < 0) or (body_score == 100 or title_score == 100)) and answer_score == 1:
            hits_and += 1
            print "sum - " + str(hits_and) + " of " + str(iterations)
        if ((title_score * 1 / 4 + body_score * 3 / 4 < 0) or (body_score == -100 or title_score == -100)) and answer_score == 0:
            hits_and += 1
            print "sum - " + str(hits_and) + " of " + str(iterations)
        # If both scores sarcastic and answer is fake
        # if title_score & body_score == answer_score:
        #     hits_and += 1
        #     print "& - " + str(hits_and) + " of " + str(iterations)
        # if title_score | body_score == answer_score:
        #     hits_or += 1
        #     print "| - " + str(hits_and) + " of " + str(iterations)

    csvfile.close()
    resultCSVFile.close()

getstuff("test-data.csv")

# percentage = evaluate.tweetscore("no sarcasm here")
# print percentage
# percentage = evaluate.tweetscore("trying to be serious")
# print percentage
# percentage = evaluate.tweetscore("no shit")
# print percentage

# print "Title Score " + str(title_score)

# body = row[5].split(" ")
# num_of_sentences = 0
# body_avg_score = 0
# curr_sentence = ""
# print evaluate.tweetscore(row[5])

# for word in body:
#     curr_sentence += word + " "
#     if len(curr_sentence) > max_chars_in_sentence:
#         body_avg_score = (body_avg_score * num_of_sentences + evaluate.tweetscore(curr_sentence)) / (num_of_sentences + 1)
#
#         # print curr_sentence
#         # print evaluate.tweetscore(curr_sentence)
#         curr_sentence = ""
#         num_of_sentences += 1
#
# # print "Body Score " + str(body_avg_score)

# article_index += 1