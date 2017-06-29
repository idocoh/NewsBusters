from sklearn.ensemble import RandomForestClassifier
from glob import glob
import cPickle as pickle
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import KFold, cross_val_score


#TRAIN_STEP = False

# change for different files (train? test?)
FILES_PATH = r'C:/Users/meita/Documents/GitHub/fnc-1/data/*'
TAG_FILE = r'tags_chen.csv'


def main():
    data = []
    x = []
    for f_name in glob(FILES_PATH):
        with open(f_name, 'rb') as reader:
            data.append(reader.readlines())
    for sample_id in range(len(data[0])):
        x.append([])
        for file_id in range(len(data)):
            if len(data[file_id][sample_id].replace("\r", "").replace("\n", "").split(",")) == 0:
                continue
            if "nan" in [str(e) for e in data[file_id][sample_id].replace("\r", "").replace("\n", "").split(",")]:
                x[sample_id] += [0] * len(data[file_id][sample_id].replace("\r", "").replace("\n", "").split(","))
            else:
                x[sample_id] += [float(e) for e in data[file_id][sample_id].replace("\r", "").replace("\n", "").split(",")]

    x = np.array(x)

    with open(TAG_FILE, 'rb') as reader:
        y = reader.readlines() # assuming 0 is legit article, 1 is fake

    y = np.array([int(e.replace("\r", "").replace("\n", "")) for e in y])

    scaler = preprocessing.StandardScaler().fit(x)
    x_scaled = scaler.transform(x)

    clf = RandomForestClassifier(n_jobs=100)
    k_fold = KFold(len(y), n_folds=3, shuffle=True, random_state=0)
    acc = cross_val_score(clf, x_scaled, y, cv=k_fold, n_jobs=1) # accuracy
    print('Acc', np.mean(acc), acc)
    pre = cross_val_score(clf, x_scaled, y, cv=k_fold, n_jobs=1, scoring='precision') # TODO: make sure it really works
    print('Pre', np.mean(pre), pre)
    rec = cross_val_score(clf, x_scaled, y, cv=k_fold, n_jobs=1, scoring='recall')
    print('Recall', np.mean(rec), rec)

    """
    if TRAIN_STEP:
        scaler = preprocessing.StandardScaler().fit(x)
        x_scaled = scaler.transform(x)
        clf = RandomForestClassifier(n_jobs=100)
        clf.fit(x_scaled, y)
        with open('clf.p', 'w') as f:
            pickle.dump(clf, f)
        with open('scaler.p', 'w') as f:
            pickle.dump(scaler, f)
    else:
        with open('clf.p','r') as f:
            clf = pickle.load(f)
        with open('scaler.p','r') as f:
            scaler = pickle.load(f)

        x_scaled = scaler.transform(x)
        prediction = clf.predict(x_scaled)
        tp = tn = fp = fn = 0
        for i in range(len(prediction)):
            if prediction[i] == y[i] == 1:
                tp += 1
            elif prediction[i] == y[i] == 0:
                tn += 1
            elif prediction[i] == 1:
                fp += 1
            elif prediction[i] == 0:
                fn += 1

        print "Precision:", tp / (tp + fn) * 100, "%"
        print "Accuracy:", (tp + tn) / (tp + tn + fp + fn) * 100, "%"
        print "Recall:", tp / (tp + fp) * 100, "%"
    """


if __name__ == "__main__":
    main()