from envtest import summarize_measurements


measurements = {
    'temperature_c': [18.2, 20.1, 19.4, 21.0],
    'rainfall_mm': [0.0, 1.2, 0.0, 4.6],
}

print(summarize_measurements(measurements))
