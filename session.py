# Write each set of responses to a separate CSV file

import pandas as pd

file_path = 'during.csv'
df = pd.read_csv(file_path)

session_data = {}
for session_id in range(1, 10):
    session_data[session_id] = df[df['Session ID (to be filled by the conductor)'] == session_id]

    
    output_file_path = f'session_{session_id}_responses.csv'
    session_data[session_id].to_csv(output_file_path, index=False)
    print(f"Responses for Session {session_id} written to {output_file_path}")

