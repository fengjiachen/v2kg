# coding=utf-8
# 使用轮廓系数SilhouetteCoefficient度量聚类结果质量
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def main():
    plt.subplot(3, 2, 1)
    x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
    x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
    
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.title('Instances')
    plt.scatter(x1, x2)
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
    markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
    
    clusters = [2, 3, 4, 5, 6]
    subplot_counter = 1
    sc_scores = []

    for t in clusters:
        subplot_counter += 1
        plt.subplot(3, 2, subplot_counter)
        kmeans_model = KMeans(n_clusters=t).fit(X)

        for i, l in enumerate(kmeans_model.labels_):
            plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l], ls=None)
        plt.xlim([0, 10])
        plt.ylim([0, 10])
        sc_score = silhouette_score(X, kmeans_model.labels_, metric='euclidean')
        print(sc_score)
        sc_scores.append(sc_score)
        plt.title('K=%s, slihouette corfficent=%0.03f' % (t, sc_score))
        
    plt.figure()
    plt.plot(clusters, sc_scores, '*-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Slihouette Coefficient Score')
    plt.show()

if __name__ == "__main__":
    main()
