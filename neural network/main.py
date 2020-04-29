from classes.gui.Table import Table
from classes.data.Analyze import Analyze


def main():
    analyze = Analyze()
    data_frame = analyze.get_data_frame_from_url("https://raw.githubusercontent.com/matebence/Mate_NS2020/master/dataset.csv")

    analyze.get_data_set_informations(data_frame)
    analyze.get_first_x_number_of_rows(5, data_frame)
    analyze.get_data_description(data_frame)

    analyze.plot_by_count(data_frame.sex.value_counts())
    analyze.plot_dataset(data_frame)

    Table().set_data_frame(analyze.transform_non_numerical_data(data_frame)).start_gui()


if __name__ == "__main__":
    main()
