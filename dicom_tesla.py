# Import the necessary library
import pydicom

# Specify the DICOM file
dicom_file = (r"PATH OF DICOM FILE")

# Read the DICOM file
ds = pydicom.dcmread(dicom_file)

# Extract the Magnetic Field Strength
tesla_strength = ds.MagneticFieldStrength

# Extract the Study Date
study_date = ds.StudyDate

# Extract the Manufacturer
manufacturer = ds.Manufacturer

print(f'Magnetic Field Strength: {tesla_strength} Tesla')
print(f'Study Date: {study_date}')
print(f'Manufacturer: {manufacturer}')

