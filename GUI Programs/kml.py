import math


def euc_distance(p1,p2):
    return math.sqrt((p1["X"] - p2["X"]) ** 2 + (p1["Y"] - p2["Y"]) ** 2 )

def mean_point(points):
    x_sum = sum(p["X"] for p in points)
    y_sum = sum(p["Y"] for p in points)

    count = len(points)

    return {"X":x_sum/count,"Y":y_sum/count}

def user_defined_kmeans():
    border = "-"*50

    data = [
        {"point":"P1","X":2,"Y":10},
        {"point":"P2","X":2,"Y":5},
        {"point":"P3","X":8,"Y":4},
        {"point":"P4","X":5,"Y":8},
        {"point":"P5","X":7,"Y":5},
        {"point":"P6","X":6,"Y":4},
    ]

    k = 2

    centroids = [
        {"X":data[0]["X"],"Y":data[0]["Y"]},
        {"X":data[3]["X"],"Y":data[3]["Y"]},
    ]

    print(border)
    print("User Defined K-means")
    print(border)

    print(border)
    print("Dataset")
    print(border)

    for d in data:
        print(d)

    print(border)
    print("Initial Centroids : ")
    print(border)

    for i,c in enumerate(centroids):
        print(f"c{i+1} : {c}")
    
    max_iterations = 10

    for itr in range(1,max_iterations + 1):
        print(border)
        print(f"Iteration {itr} : ")
        print(border)

        clusters = {0:[],1:[]}

        for p in data:
            dist_list = [euc_distance(p,c) for c in centroids]

            nearest_centroid_index = dist_list.index(min(dist_list))

            clusters[nearest_centroid_index].append(p)

        print("Cluster Assignment : ")
        for cluster_id in clusters:
            names = [pt["point"] for pt in clusters[cluster_id]]
            print(f"Cluster {cluster_id + 1} : {names}")


        new_centroids = []

        for cluster_id in range(k):
            if len(clusters[cluster_id]) == 0:
                new_centroids.append(centroids[cluster_id])
            else:
                new_centroids.append(mean_point(clusters[cluster_id]))

        print("Updated Centroids : ")    
        for i, c in enumerate(new_centroids):
            print(f"C{i+1} : {c}")

        if new_centroids == centroids:
            print(border)
            print("Converged : centroids unchanged. Stopping...")  
            print(border)
            break

        centroids = new_centroids

    
    # Final Centroids 

    print(border)
    print("Final Result")
    print(border)

    for cluster_id in clusters:
        names = [pt["point"] for pt in clusters[cluster_id]]
        print(f"Cluster {cluster_id + 1} : {names}")
    
    print(border)
    print("Final Centroids : ")
    print(border)

    for i,c in enumerate(centroids):
        print(f"C{i + 1} : {c}")


def main():
    user_defined_kmeans()

main()