import json

import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = json.load(open("sarco_performance.json"))

    fig = plt.figure()

    plt.plot(data["sizes"], data["scratch_mae"], label="Trained from scratch")
    plt.plot(data["sizes"], data["pretrain_mae"], label="Pre-Trained")
    plt.legend()
    plt.show()
