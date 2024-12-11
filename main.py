import yfinance as yf
import torch
from kan import *

if __name__ == "__main__":

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(device)
    model = KAN(width=[2,1,1], grid=3, k=3, seed=1, device=device)

    datapoints_data = pd.read_csv('data/small_mkt_cap/bb.csv')[['Open', 'Volume']].values.astype(np.float32)
    labels_data = pd.read_csv('data/small_mkt_cap/bb.csv')['Close'].values.astype(np.float32)

    train_input = torch.tensor(datapoints_data[:int(0.8*len(datapoints_data)), :])
    test_input = torch.tensor(datapoints_data[int(0.8*len(datapoints_data)):, :])

    train_label = torch.tensor(labels_data[:int(0.8*len(datapoints_data))])
    test_label = torch.tensor(labels_data[int(0.8*len(datapoints_data)):])

    dataset = {}
    dataset['train_input'] = train_input.to(device)
    dataset['test_input'] = test_input.to(device)

    dataset['train_label'] = train_label.to(device)
    dataset['test_label'] = test_label.to(device)

    model.fit(dataset, opt="LBFGS", steps=20)