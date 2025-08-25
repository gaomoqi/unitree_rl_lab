# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for Unitree robots.

Reference: https://github.com/unitreerobotics/unitree_ros
"""

from dataclasses import MISSING

import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg, ImplicitActuatorCfg  # noqa: F401
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils import configclass


@configclass
class UnitreeArticulationCfg(ArticulationCfg):
    """Configuration for Unitree articulations."""

    joint_sdk_names: list[str] = None


UNITREE_MODEL_DIR = "/home/moqi.gao/unitree_rl_lab/unitree_model"

UNITREE_H21_CFG = UnitreeArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{UNITREE_MODEL_DIR}/H21/usd/h21_10dof_0717.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.48), #0.49325
        joint_pos={
            "right_hip_pitch_joint": -0.15,
            "right_hip_roll_joint": 0.0,
            "right_hip_yaw_joint": 0.0,
            "right_knee_joint": 0.4,
            "right_foot_joint": -0.2,
            "left_hip_pitch_joint": -0.15,
            "left_hip_roll_joint": 0.0,
            "left_hip_yaw_joint": 0.0,
            "left_knee_joint": 0.4,
            "left_foot_joint": -0.2,
        },
        # joint_pos={
        #     "right_hip_pitch_joint": -0.0,
        #     "right_hip_roll_joint": 0.0,
        #     "right_hip_yaw_joint": 0.0,
        #     "right_knee_joint": 0.0,
        #     "right_foot_joint": 0.0,
        #     "left_hip_pitch_joint": 0.0,
        #     "left_hip_roll_joint": 0.0,
        #     "left_hip_yaw_joint": 0.0,
        #     "left_knee_joint": 0.0,
        #     "left_foot_joint": 0.0,
        # },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_yaw_joint",
                ".*_hip_roll_joint",
                ".*_hip_pitch_joint",
                ".*_knee_joint",
            ],
            effort_limit_sim={
                ".*_hip_yaw_joint": 10.0,
                ".*_hip_roll_joint": 10.0,
                ".*_hip_pitch_joint": 7.0,
                ".*_knee_joint": 10.0,
            },
            velocity_limit_sim={
                ".*_hip_yaw_joint": 10.0,
                ".*_hip_roll_joint": 10.0,
                ".*_hip_pitch_joint": 10.0,
                ".*_knee_joint": 10.0,
            },
            stiffness = {
                ".*hip_pitch_joint": 40.0,
                ".*hip_roll_joint": 20.0,
                ".*hip_yaw_joint": 20.0,
                ".*knee_joint": 40.0,
            },
            damping={
                ".*hip_pitch_joint": 0.6,
                ".*hip_roll_joint": 0.4,
                ".*hip_yaw_joint": 0.4,
                ".*knee_joint": 0.6,
            }
        ),

        "feet": ImplicitActuatorCfg(
            joint_names_expr=[".*_foot_joint"],
            effort_limit_sim=7.0,
            velocity_limit_sim=9.0,
            stiffness=40.0,
            damping=0.6,
        ),
        
    },
)

#     joint_sdk_names=[
#         "right_hip_roll_joint",
#         "right_hip_pitch_joint",
#         "right_knee_joint",
#         "left_hip_roll_joint",
#         "left_hip_pitch_joint",
#         "left_knee_joint",
#         "torso_joint",
#         "left_hip_yaw_joint",
#         "right_hip_yaw_joint",
#         "",
#         "left_ankle_joint",
#         "right_ankle_joint",
       
#     ],
# )

