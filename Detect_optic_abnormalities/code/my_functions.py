import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.metrics import confusion_matrix, recall_score, precision_score, roc_auc_score, accuracy_score, roc_curve

#Prints basic information about dataframe
def basic_eda(df, name):

	print("DATAFRAME INFORMATION")
	print(f"---------------------------------------")
	print(f"Rows: {df.shape[0]}             Columns: {df.shape[1]}")
	print(f'Duplicated rows: {(df.duplicated(keep=False) == True).sum()}')
	print(f'Columns:')
	print(f"""{pd.concat([
		pd.DataFrame(data=df.dtypes, columns=['data_type']), 
		pd.DataFrame(data=df.isnull().sum(), columns=['num_nulls']), 
		pd.DataFrame(data=df.notnull().sum(), columns=['num_not_nulls']), 
		pd.DataFrame(data=df.nunique(), columns=['unique_values'])], axis=1)} \n""")
	

#inputs data into subplots
def subplot_data(ax, ax_ravel, title, xlabel, ylabel):
    ax[ax_ravel].set_title(title, fontsize=16, fontweight='bold')
    ax[ax_ravel].set_xlabel(xlabel, fontsize=14)
    ax[ax_ravel].set_ylabel(ylabel, fontsize=14)
    ax[ax_ravel].tick_params(axis='both', labelsize=14)


#function to read NPZfiles
#allow pickle to get item access
def read_npz(filepath):
    npz_file = np.load(file=filepath, allow_pickle=True)
    img_variable = npz_file.get(npz_file.files[0])
    img_variable = np.asarray(img_variable.tolist())
    print(f"Array shape: {img_variable.shape}")
    return img_variable

def sample_category_images(col_name, num_cols, df, filepath):  
    """
    Parameters:
    col_name: column name with categories
    num_cols: number of samples per category; 
              image categories (row) x number of samples (column)
    df: dataframe containing "col_name"
    filepath: filepath column in dataframe
    DocString:
    Displays specified number of images (column) per category (row)
    """
    categories = (df.groupby([col_name])[col_name].nunique()).index
    fig, ax = plt.subplots(nrows=len(categories),ncols=num_cols, 
                         figsize=(4*num_cols,4*len(categories))) #size 4 per image
    # Sample of images for each category
    for i, cat in enumerate(categories):
        sample = df[df[col_name]==cat].sample(num_cols)
        #iterating through sample per category
        for j in range(0,num_cols):
            
            #For image labelling
            if cat == 1:
                cat = "Abnormal"
            elif cat == 0:
                cat = "Normal"
            if filepath == 'filepath':
                #opens image based on filepath in sample dataframe
                im=Image.open(sample[filepath].iloc[j])
            else: 
                im = sample[filepath].iloc[j]
            ax[i, j].imshow(im, resample=True)
            ax[i, j].set_title(cat, fontsize=16)  
    plt.tight_layout()
    plt.show()



# Plots training and validation loss, and training and validation accuracy over epochs
def plot_history(model_history, train, validation, metric, ylabel):
    # Generate line plot of training, validation loss over epochs.
    plt.figure(figsize=(14,7))
    plt.plot(model_history.history[train], label=f'Train {metric} ' )
    plt.plot(model_history.history[validation], label=f'Validation {metric} ')
    plt.title(f'Training and Validation {metric} by Epoch', fontsize = 16)
    plt.xlabel('Epoch', fontsize = 11)
    plt.ylabel(ylabel, fontsize = 11)
    plt.tick_params(axis='both', labelsize=11)
    plt.legend(fontsize = 11)
    # plt.set_ylim(0,1)


#define function to print performance metrics
def perf_metrics(y_true, y_pred):
    #Generate a confusion matrix
    tn, fp, fn, tp = confusion_matrix(y_test, preds).ravel()
    # print categories
    print("True Negatives: %s" % tn)
    print("False Positives: %s" % fp)
    print("False Negatives: %s" % fn)
    print("True Positives: %s" % tp)
    
    #compute metrics
    accuracy = round(accuracy_score(y_true, y_pred),4)
    misclassification = round((1 - accuracy),4)
    specificity = round(recall_score(y_true, y_pred, pos_label=0),4)
    recall = round(recall_score(y_true, y_pred, pos_label=1),4)
    precision = round(precision_score(y_true, y_pred),4)
    roc_auc = round(roc_auc_score(y_true, y_pred),4)
    f1_score = round((2 * precision * recall) / (precision + recall),4)

    print("")
    #print metrics
    print('PERFORMANCE METRICS')
    print('---------------------')
    print(f'Accuracy: {accuracy}')
    print(f'Misclassification: {misclassification}')
    print(f'Specificity: {specificity}')
    print(f'Sensitivity/Recall: {recall}')
    print(f'Precision: {precision}')
    print(f'ROC-AUC: {roc_auc}')
    print(f'F1-score: {f1_score}')

    return tn, fp, fn, tp, accuracy, misclassification, specificity, recall, precision, roc_auc, f1_score