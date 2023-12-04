import pydicom

def extract_metadata(dicom_file, txt_file):
    # Load the DICOM file
    ds = pydicom.dcmread(dicom_file)

    # Open the text file
    with open(txt_file, 'w') as f:
        # Iterate over the DICOM dataset's elements
        for elem in ds.iterall():
            # Write the element's tag, VR, and value to the text file
            f.write(f"{elem.tag} {elem.VR}: {elem.value}\n")

# Use the function
extract_metadata('path_to_your_dicom_file.dcm', 'output.txt')

