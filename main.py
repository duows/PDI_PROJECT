from utils import read_video, save_video
from trackers import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
import numpy as np
import cv2

modelPath = 'C:/Users/henri/PROJETO_PDI/PDI_PROJECT/training/runs/detect/modelv3/weights/best.pt'

def main():
    # ler video
    video_frames = read_video('C:/Users/henri/PROJETO_PDI/PDI_PROJECT/input_video/video_spfc.mp4')

    tracker = Tracker(modelPath)

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=False, stub_path='C:/Users/henri/PROJETO_PDI/PDI_PROJECT/stubs/track_stubs.pkl')

    tracks['ball'] = tracker.interpolate_ball_positions(tracks['ball'])

    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

    for frame_number, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_number], track['bbox'], player_id)     

            tracks['players'][frame_number][player_id]['team'] = team
            tracks['players'][frame_number][player_id]['team_color'] = team_assigner.team_colors[team]

    # for track_id, player in tracks['players'][0].items():

    #     bbox = player['bbox']
    #     frame = video_frames[0]

    #     cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

    #     cv2.imwrite(f'output_video/player_{track_id}.jpg', cropped_image)

    #     break
        
    player_assigner =PlayerBallAssigner()
    team_ball_control= []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])
    team_ball_control= np.array(team_ball_control)

    output_video_frames = tracker.draw_annotations(video_frames, tracks,team_ball_control)

    # salvar video
    save_video(output_video_frames, 'C:/Users/henri/PROJETO_PDI/PDI_PROJECT/output_video/output.avi')

if __name__ == '__main__':
    main()