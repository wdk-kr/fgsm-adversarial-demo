# 🧠 FGSM Adversarial Demo

본 프로젝트는 **딥러닝 이미지 분류 모델의 취약성**을 직접 체험해볼 수 있도록 만든 **FGSM 적대적 공격 데모 웹 도구**입니다.  
고등학교 프로젝트로 진행되었으며, 누구나 쉽게 접근할 수 있도록 **Streamlit 기반 웹 UI**로 제작되었습니다.

### 🔗 체험 링크  
👉 [https://fgsm.wdk.kr](https://fgsm.wdk.kr) 에서 직접 실행해보실 수 있습니다.

---

### ✅ 기능 소개

- 이미지 분류 모델(MobileNetV2)에 대해 **FGSM(Fast Gradient Sign Method)** 공격 실험 가능  
- 예제 이미지 제공 또는 사용자 이미지 업로드 지원  
- ε (epsilon) 값을 조절하며 공격 강도를 실시간으로 테스트  
- 원본 / 공격 이미지에 대한 분류 결과 비교

---

### 🛠 실행 방법

1. **웹에서 사용**  
   - 별도 설치 없이 [fgsm.wdk.kr](https://fgsm.wdk.kr) 접속 후 바로 사용

2. **로컬에서 실행**  
   - Python 환경에서 직접 실행하거나, 제공된 `Dockerfile`로 이미지 빌드 후 구동 가능

---

### 🖼 미리보기

![FGSM Demo Screenshot](https://github.com/user-attachments/assets/b14eb6ed-35bf-4b5d-9d78-836ce75e9320)

---

### 📄 참고

- 본 도구는 TensorFlow의 MobileNetV2 모델을 기반으로 제작되었으며, 학습된 ImageNet 가중치를 사용합니다.
- FGSM 알고리즘 및 구현은 [TensorFlow 공식 튜토리얼](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)을 참조하였습니다.

