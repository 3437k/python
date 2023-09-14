# 비디오, 자막 목록 가져와서 크기 비교, 일치시 비디오 목록 기준으로 이름 변경 
# 비디오_이름.en.srt
# video_folder, subtitle_folder 위치 변경 필요 

import os

# 비디오 파일 폴더 위치
video_folder = "./"

# 자막 파일 위치 
subtitle_folder = "./srt"

# 비디오 목록 추출
video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.mkv', '.avi'))]

# 비디오 목록 길이 
print(f'비디오파일 {len(video_files)}개 발견')

# 자막 목록 추출
subtitle_files = [f for f in os.listdir(subtitle_folder) if f.endswith('.srt')]
print(f'자막파일 {len(subtitle_files)}개 발견')


if(len(video_files) == len(subtitle_files)):
    print("비디오와 자막 파일 개수 일치")

    for i in range(len(video_files)):
        video_file = video_files[i]
        subtitle_file = subtitle_files[i]

        # 비디오 파일 이름에서 확장자 제거
        video_name, _ = os.path.splitext(video_file)

        # 자막 파일 이름 생성
        new_subtitle_name = f'{video_name}.en.srt'
        
        # 새 자막 파일 경로 생성
        new_subtitle_path = os.path.join(subtitle_folder, new_subtitle_name)

        # 자막 파일 이름 변경
        os.rename(os.path.join(subtitle_folder, subtitle_file), new_subtitle_path)
        print(f'Renamed {subtitle_file} to {new_subtitle_name}')

    
