import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch


def iou_from_model(data_loader: torch.utils.data.DataLoader,
                   model,
                   device):
    """ Calculate IOU using the input model and data_loader
    Args:
        data_loader:
            torch.utils.data.DataLoader
        model:
            torch model
        device: str
            'cpu' or 'cuda'

    Returns:
    list of IOU for each input data set using the model
    """
    iou_list = []
    model.eval()
    with torch.no_grad():
        for sample in data_loader.dataset:
            image, target = sample
            box_pred = model([image.to(device)])[0]
            if len(box_pred['boxes']):
                box_pred = box_pred['boxes'][0, :]
            else:
                continue
            box_true = target['boxes']
            iou_list.append(bb_intersection_over_union(
                np.squeeze(box_true.cpu().numpy()),
                np.squeeze(box_pred.cpu().numpy())))
    return iou_list


def bb_intersection_over_union(boxA, boxB):
    """Box-Box intersection over union utils
    Calculate the IOU for two bounding boxes with same size.
    Each box is represented by its diagonal points.
    Args:
        boxA:
            Box 1 (x_min, y_min, x_max, y_max)
        boxB:
            Box 2 (x_min, y_min, x_max, y_max)

    Returns:
    IOU for boxA and boxB
    """
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA) * max(0, yB - yA)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    # return the intersection over union value
    return iou


def plot_iou(data_loader: torch.utils.data.DataLoader,
             model,
             device,
             image_index=None,
             random_sample=5,
             save_fig=False):
    """ Plot IOU using the input model and data_loader
    Args:
        data_loader:
            torch.utils.data.DataLoader
        model:
            torch model
        device: str
            'cpu' or 'cuda'
        image_index: int or None
            the index from dataloader to be plot
        random_sample:
            # of sample to be randomly choose if image_index is None
        save_fig:
            save the fig to the current location

    Returns:
    Matplotlib ax object
    """
    if image_index:
        num_sub_plot = 1
        image_indices = [image_index]
    else:
        num_sub_plot = random_sample
        image_indices = np.random.choice(len(data_loader.dataset), size=random_sample, replace=False)

    fig, axs = plt.subplots(num_sub_plot, figsize=(15, 10 * num_sub_plot))

    with torch.no_grad():
        for i in range(num_sub_plot):
            image, target = data_loader.dataset[image_indices[i]]
            box_pred = model([image.to(device)])[0]
            if len(box_pred['boxes']):
                box_pred = box_pred['boxes'][0, :]
            else:
                continue
            box_true = target['boxes']

            box_true = np.squeeze(box_true.cpu().numpy())
            box_pred = np.squeeze(box_pred.cpu().numpy())

            image = image.cpu().numpy().transpose(1, 2, 0)
            image = cv2.UMat(image).get()
            image_with_box_true = cv2.rectangle(image,
                                                (int(box_true[0]), int(box_true[1])),
                                                (int(box_true[2]), int(box_true[3])),
                                                (0, 1, 0),
                                                2)

            image_with_box_pred = cv2.rectangle(image_with_box_true,
                                                (int(box_pred[0]), int(box_pred[1])),
                                                (int(box_pred[2]), int(box_pred[3])),
                                                (0, 0, 1),
                                                2)
            if image_index:
                axs.imshow(image_with_box_pred)
            else:
                axs[i].imshow(image_with_box_pred)
        if save_fig:
            plt.savefig('IOU_Plots.png')
        plt.show()
