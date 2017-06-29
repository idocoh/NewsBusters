with open("deep_learning_model/deepoutput.csv", 'rb') as reader:
    res = reader.readlines()

with open("deep_learning_model/train_chen.csv", 'rb') as reader:
    y_full = reader.readlines()

# 'Agree', 'Disagree','Discuss','Unrelated'
preds = []
y = []
for line in res:
    l = line.replace("\r", "").replace("\n", "").split(",")
    if len(l) == 0:
        continue
    max_val = 0
    max_index = 0
    for i, r in enumerate(l):
        if r > max_val:
            max_val = r
            max_index = i
    if max_index == 0:
        pred = 'agree'
    if max_index == 1:
        pred = 'disagree'
    # TODO: change and check
    if max_index == 2:
        pred = 'agree'
    if max_index == 3:
        pred = 'disagree'
    preds.append(pred)

for line in y_full[1:]:
    y.append(line.replace("\r", "").replace("\n", "").split(",")[2])

tp = tn = fp = fn = 0
for i in range(len(preds)):
    if preds[i] == y[i] == 'disagree':
        tp += 1
    elif preds[i] == y[i] == 'agree':
        tn += 1
    elif preds[i] == 'disagree':
        fp += 1
    elif preds[i] == 'agree':
        fn += 1

print "Precision:", float(tp) / (tp + fn) * 100, "%"
print "Accuracy:", float(tp + tn) / (tp + tn + fp + fn) * 100, "%"
print "Recall:", float(tp) / (tp + fp) * 100, "%"