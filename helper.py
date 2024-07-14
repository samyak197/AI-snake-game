# import matplotlib.pyplot as plt
# from IPython import display

# plt.ion()


# def plot(scores, mean_scores, mean_last_35_scores, plot_label):
#     display.clear_output(wait=True)
#     display.display(plt.gcf())
#     plt.clf()
#     plt.title(f"Training {plot_label}")
#     plt.xlabel("Number of Games")
#     plt.ylabel("Score")
#     plt.plot(scores, label="Score")
#     plt.plot(mean_scores, label="Mean Score")
#     plt.plot(mean_last_35_scores, label="Mean Last 35 Scores")
#     plt.ylim(ymin=0)
#     plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
#     plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
#     plt.text(
#         len(mean_last_35_scores) - 1,
#         mean_last_35_scores,
#         str(mean_last_35_scores[-1]),
#     )
#     plt.legend()
#     plt.draw()
#     plt.pause(0.001)


import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title("Training...")
    plt.xlabel("Number of Games")
    plt.ylabel("Score")
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(0.1)


plt.ioff()


def plot_comparison(
    scores_1layer,
    scores_3layers,
    save_path="C:/Users/samya/OneDrive/Desktop/New folder (2)/MakeMore/game/model_comparison.png",
):
    plt.figure(figsize=(12, 6))
    plt.title("Model Comparison")
    plt.xlabel("Number of Games")
    plt.ylabel("Score")
    plt.plot(scores_1layer, label="without score Model")
    plt.plot(scores_3layers, label="with score Model")
    plt.ylim(ymin=0)
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
