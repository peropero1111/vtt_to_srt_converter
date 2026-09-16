# vtt_to_srt_converter
영상 관련 일 취미로 하고 있는데 vtt는 인코딩이 안 되길래 변환기 만들었습니다. 

<br>

### 이 프로그램은 python 3.14 버젼에서 작성되었습니다.  
따라서 그보다 낮은 버젼에선 정확하게 작동하지 아니할 수 있으며 이에 대한 대처는 어려운점 양해 부탁드립니다.

- - -


### 목차
1. [python 으로 시작하기](#python-으로-시작하기)
2. [exe 로 시작하기](#exe-로-시작하기)
3. [기능 소개](#기능-소개)

-  - -

## python 으로 시작하기
<br>
먼저 이 레퍼지토리 를 zip 파일로 다운하신 뒤 <code>converter.py</code>를 편하신 ide 에서 열어주십시오
<br>
<br>

- - -

## exe 로 시작하기
<br>

[이 링크를 통해](https://drive.google.com/drive/folders/1QnEglaxZhwIP6_-X57JxMZkDydHMXXC6?usp=sharing) exe 파일을 다운 받으십시오.
<br>
<br>

--- 

## 기능 소개 
<br>


이 .py 프로그램을 실행 시키신 뒤 <code>.vtt</code> 파일이 위치한 경로로 이동하십시오.  
</br>
<img src="https://github.com/peropero1111/vtt_to_srt_converter/blob/main/img/2026-09-16%20231747.png?raw=true" width="450" height="450"/> 

</br>
</br>
그 다음 <code>.vtt</code> 파일을 고른 후 .srt 파일이 출력될 폴더를 고르시면 됩니다.
</br>
</br>
<img src="https://github.com/peropero1111/vtt_to_srt_converter/blob/main/img/2026-09-16%20231854.png?raw=true" width="450" height="450"/><img src="https://github.com/peropero1111/vtt_to_srt_converter/blob/main/img/2026-09-16%20231854.png?raw=true" width="450" height="450"/> 



</br>
</br>
다음은 정상적으로 출력된 .srt 파일과 기존의 .vtt 파일의 비교 입니다. 
<br>
<br>
<img src="https://github.com/peropero1111/vtt_to_srt_converter/blob/main/img/2026-09-16%20232007.png?raw=true" width="450" height="450"/><img src="https://github.com/peropero1111/vtt_to_srt_converter/blob/main/img/2026-09-16%20232026.png?raw=true" width="450" height="450"/>  

</br>
아래에 자세한 사용방법 영상이 첨부 되어 있습니다.
</br>
</br>



https://github.com/user-attachments/assets/bc831531-bb6e-4a8d-91aa-384bf03b9d51


</br>
</br>

- - -
</br>


## 면책조항

이 소프트웨어는 어떠한 종류의 명시적 또는 묵시적 보증 없이
**"있는 그대로(AS IS)"** 제공됩니다.

`vtt_to_srt_converter`는 WebVTT(`.vtt`) 자막 파일을 SubRip(`.srt`)
형식으로 변환하기 위한 간단한 보조 도구입니다.

프로젝트 작성자는 다음 사항을 보장하지 않습니다.

* 모든 VTT 파일이 정상적으로 변환되는 것
* 모든 WebVTT 기능, 태그 또는 메타데이터가 SRT 형식으로 그대로 보존되는 것
* 변환된 자막의 타이밍, 줄바꿈 또는 내용이 원본과 완전히 동일한 것
* 모든 자막 프로그램 및 미디어 플레이어에서 동일하게 작동하는 것
* 프로그램이 모든 환경에서 오류 없이 작동하는 것

중요한 자막 파일을 변환하기 전에는 원본 파일의 백업을 보관하고,
변환 후에는 생성된 SRT 파일의 내용과 타이밍을 직접 확인하는 것을
권장합니다.

이 소프트웨어의 사용 또는 사용 불가능으로 인해 발생하는 데이터 손실,
자막 오류 또는 기타 손해에 대한 책임은 저장소의 `LICENSE`에 규정된
범위 내에서 제한됩니다.

