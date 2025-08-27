import pygame
import math
import sys

# ===============================
# 클래스 정의
# ===============================

class CelestialBody:
    def __init__(self, name, mass, x, y, vx, vy, radius, color):
        # 이름, 질량, 위치, 속도, 반지름, 색상 저장
        pass

    def apply_force(self, fx, fy, dt):
        # 힘을 받아 속도 갱신
        pass

    def update_position(self, dt):
        # 속도에 따라 위치 갱신
        pass

    def record_path(self):
        # 현재 위치를 궤도 리스트에 추가
        pass

    def draw(self, screen):
        # 화면에 천체와 궤도를 그림
        pass


# ===============================
# 함수 정의
# ===============================

def compute_gravitational_force(body1, body2, G):
    # 두 천체 사이의 중력 벡터를 계산하여 반환
    pass

def create_orbiting_body(center_body, distance, mass, radius, color, G):
    # 중심 천체를 기준으로 일정 거리에서 원운동하는 천체 생성
    # 초기 속도 계산 후 CelestialBody 반환
    pass


# ===============================
# 메인 루프
# ===============================

def main():
    # pygame 초기화
    # 화면 크기 설정
    # 시계(clock) 객체 생성
    # 중력 상수 G, 시간 간격 dt 설정
    
    # 천체 리스트 초기화
    # 태양 생성
    # 행성 몇 개 생성 후 리스트에 추가

    running = True
    while running:
        # 이벤트 처리 (종료 버튼 등)
        
        # 배경 지우기
        
        # 모든 천체 쌍에 대해 중력 계산
        # 각 천체에 힘 적용
        # 각 천체 위치 업데이트
        # 각 천체 궤도 기록
        # 각 천체 그리기

        # 화면 갱신
        # FPS 맞추기

    # pygame 종료


if __name__ == "__main__":
    main()

