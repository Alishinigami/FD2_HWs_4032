# سوال یک
import math

def circular_turn_motion(speed, bank_angle):
    g = 9.81  #  جاذبه زمین
    bank_angle_rad = math.radians(bank_angle)  # تبدیل زاویه به رادیان

    # محاسبه شعاع چرخش
    R = (speed ** 2) / (g * math.tan(bank_angle_rad))

    # محاسبه سرعت زاویه‌ (امگا)
    angular_velocity = speed / R

    # ایجاد دیکشنری خروجی
    return {
        "Angular_velocity_in_inertial_frame": [0, 0, angular_velocity],
        "Angular_velocity_in_body_frame": [0, angular_velocity, 0]
    }

# تست تابع
result = circular_turn_motion(250, 60)
print(result)
# سوال دو
import numpy as np
from scipy.spatial.transform import Rotation as R

def euler_angles_from_angular_velocity(omega_vector):
    p, q, r = omega_vector

    # تقریباً زوایه های اویلر را تخمین می‌زنیم
    phi = np.arctan2(q, r)
    theta = np.arcsin(-p / np.linalg.norm(omega_vector))
    psi = np.arctan2(q, p)

    euler_angles = [np.degrees(phi), np.degrees(theta), np.degrees(psi)]

    # نرخ تغییر زوایه های اویلر (با تقریب اولیه)
    euler_angles_rate = [p, q, r]

    return {
        "Euler_angles": euler_angles,
        "Euler_angles_rate": euler_angles_rate
    }

# تست تابع
omega_input = [0.33, 0.28, 0.16]
result = euler_angles_from_angular_velocity(omega_input)
print(result)
#سوال سه
import numpy as np
from scipy.spatial.transform import Rotation as R

def analyze_rotation_matrix(C):
    # بررسی شرایط ماتریس انتقال
    det_C = np.linalg.det(C)
    is_rotation_matrix = np.allclose(np.dot(C, C.T), np.eye(3)) and np.isclose(det_C, 1)

    if not is_rotation_matrix:
        return "ماتریس ورودی شرایط یک ماتریس انتقال را ندارد."

    # محاسبه بردار کواترنیون
    rotation = R.from_matrix(C)
    quaternion_vector = rotation.as_quat().tolist()

    # محاسبه زوایای اویلر
    euler_angles = rotation.as_euler('xyz', degrees=True).tolist()

    # محاسبه بردار دوران
    rotation_vector = rotation.as_rotvec().tolist()

    return {
        "Quaternion_vector": quaternion_vector,
        "Euler_angles": euler_angles,
        "Rotation_vector": rotation_vector
    }

# تست تابع
C_matrix = np.array([
    [0.2802, 0.1387, 0.9499],
    [0.1962, 0.9603, -0.1981],
    [-0.9397, 0.2418, 0.2418]
])

result = analyze_rotation_matrix(C_matrix)
print(result)