# silent-video-subtitle-maker
Paste in paragraphs and this script will chop it up into subtitles.

# Planned execution flow
User pastes in a script and hits "generate" button
Split the script into a list L of individual sentences
Initialize start timestamp at 00:00:00
For each sentence in L, estimate how long it will take to read
    Attach a start timestamp (current timestamp counter) and end timestamp
    Update current timestamp counter to end timestamp
Create and open vtt file (from filename entered by user), write mode
    For each sentence/start/end write to vtt file in specified format (Batch and do 1 write)
Close file
Notify user

# Rules for splitting
Split sentences
If sentences are too long, split in half
If sentences are too short, see if the following sentences are also short and lump them together accordingly
1 big string -> List of split strings -> List of subtitle objects (calculate time) -> Write to file
