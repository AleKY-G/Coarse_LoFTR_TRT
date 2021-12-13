import argparse
from train.trainer import Trainer
from train.settings import TrainSettings


def main():
    parser = argparse.ArgumentParser(description='LoFTR knowledge distillation.')
    parser.add_argument('--path', type=str, default='/mnt/f405a161-1440-4419-9adf-1959bb1db1b2/data_sets/BlendedMVS',
                        help='Path to the dataset.')
    parser.add_argument('--checkpoint_path', type=str,
                        default='/mnt/f405a161-1440-4419-9adf-1959bb1db1b2/development/models/LoFTR',
                        help='Path to the dataset.')
    parser.add_argument('--weights', type=str, default='weights/outdoor_ds.ckpt',
                        help='Path to the LoFTR teacher network weights.')

    opt = parser.parse_args()
    print(opt)

    settings = TrainSettings()
    trainer = Trainer(settings, opt.weights, opt.path, opt.checkpoint_path)
    trainer.train('LoFTR')


if __name__ == '__main__':
    main()
