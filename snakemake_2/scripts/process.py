import pandas as pd

#def print_data(df):
#    print(df)

if __name__ == "__main__":
    #print(snakemake.log[0])
    df = pd.read_csv(snakemake.input.data)
    df.head().to_csv(snakemake.output.out)
    # print("test")
