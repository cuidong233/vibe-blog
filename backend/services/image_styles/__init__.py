"""
图片风格管理模块

提供多风格博客配图的管理功能，支持：
- 风格配置管理（styles.yaml）
- Jinja2 Prompt 模板渲染
- 风格列表查询（供前端下拉框使用）
"""

from .manager import ImageStyleManager, get_style_manager

__all__ = ['ImageStyleManager', 'get_style_manager']
