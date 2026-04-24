import io
import time
from PIL import Image, ImageFilter
from dataclasses import dataclass
from typing import Optional

@dataclass
class PrintArea:
    x: int
    y: int
    width: int
    height: int

@dataclass
class PerspectiveConfig:
    angle_x: float = 0.0
    angle_y: float = 0.0
    matrix: Optional[list] = None

@dataclass
class RenderConfig:
    blend_opacity: float = 0.92
    displacement_strength: float = 15.0
    output_quality: int = 95

class ProductRenderer:
    def render(self, base_image, user_design, print_area, 
               perspective=None, displacement_map=None, config=None):
        config = config or RenderConfig()
        t_total = time.perf_counter()

        # Resize design to print area
        design = user_design.resize(
            (print_area.width, print_area.height), Image.LANCZOS
        )

        # Blend design onto base
        result = base_image.copy().convert('RGBA')
        design_rgba = design.convert('RGBA')

        # Apply opacity
        r, g, b, a = design_rgba.split()
        a = a.point(lambda p: int(p * config.blend_opacity))
        design_rgba.putalpha(a)

        result.paste(design_rgba, (print_area.x, print_area.y), design_rgba)
        final = result.convert('RGB')

        total_ms = int((time.perf_counter() - t_total) * 1000)
        return type('RenderResult', (), {
            'image': final,
            'render_time_ms': total_ms,
            'stages': {}
        })()

    def render_to_bytes(self, result, fmt='JPEG', quality=95):
        buf = io.BytesIO()
        result.image.save(buf, format=fmt, quality=quality)
        buf.seek(0)
        return buf.read()