import numpy as np

# Function to divide the data into bins with equal depth
def create_bins(data, num_bins):
    # Sort the data
    sorted_data = np.sort(data)
    
    # Calculate bin size (approx. equal number of elements per bin)
    bin_size = len(sorted_data) // num_bins
    
    # Create bins by splitting the sorted data
    bins = [sorted_data[i * bin_size : (i + 1) * bin_size] for i in range(num_bins)]
    
    # Add remaining elements to the last bin if needed
    remainder = len(sorted_data) % num_bins
    if remainder != 0:
        bins[-1] = np.concatenate((bins[-1], sorted_data[-remainder:]))
    
    return bins

# Function to perform binning by mean
def bin_by_mean(bins):
    binned_data = [np.full(len(bin_), np.mean(bin_)) for bin_ in bins]
    return binned_data

# Function to perform binning by median
def bin_by_median(bins):
    binned_data = [np.full(len(bin_), np.median(bin_)) for bin_ in bins]
    return binned_data

# Function to perform binning by boundaries
def bin_by_boundaries(bins):
    binned_data = []
    for bin_ in bins:
        min_value, max_value = np.min(bin_), np.max(bin_)
        bin_transformed = [min_value if abs(x - min_value) < abs(x - max_value) else max_value for x in bin_]
        binned_data.append(bin_transformed)
    return binned_data

# Main function
def main():
    # Take data input from the user
    data = np.array(list(map(float, input("Enter the data values separated by spaces: ").split())))
    num_bins = int(input("Enter the number of bins: "))
    
    print("\nOriginal data:", data)
    
    # Create bins
    bins = create_bins(data, num_bins)
    print("\nBins (Equal-depth partitioning):")
    for bin_ in bins:
        print("Bin:", bin_)
    
    # Binning by mean
    mean_bins = bin_by_mean(bins)
    print("\nBinning by Mean:")
    for bin_ in mean_bins:
        print("Bin:", bin_)
    
    # Binning by median
    median_bins = bin_by_median(bins)
    print("\nBinning by Median:")
    for bin_ in median_bins:
        print("Bin:", bin_)
    
    # Binning by boundaries
    boundary_bins = bin_by_boundaries(bins)
    print("\nBinning by Boundaries:")
    for bin_ in boundary_bins:
        print("Bin:", [float(x) for x in bin_])

if __name__ == "__main__":
    main()
