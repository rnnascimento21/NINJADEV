import pygame
import random
import math
import sys

# ==============================================================================
# 1. INICIALIZAÇÃO DO SISTEMA E CONFIGURAÇÕES GERAIS
# ==============================================================================
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1100, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ninja Dev 3D - Next-Gen Commercial Edition")
clock = pygame.time.Clock()
FPS = 60

# ==============================================================================
# 2. PALETA DE CORES E DESIGN SYSTEM
# ==============================================================================
COLOR_BG_DARK = (8, 11, 18)
COLOR_BG_VSCODE = (24, 24, 24)
COLOR_VSCODE_SIDEBAR = (45, 45, 45)
COLOR_VSCODE_TAB = (38, 38, 38)
COLOR_VSCODE_TAB_ACTIVE = (24, 24, 24)

COLOR_WHITE = (245, 247, 250)
COLOR_CYAN = (0, 243, 255)
COLOR_CYAN_GLOW = (0, 243, 255, 60)
COLOR_RED = (255, 42, 109)
COLOR_GREEN = (0, 230, 118)
COLOR_GOLD = (255, 193, 7)
COLOR_GRAY = (35, 45, 65)
COLOR_MUTED = (139, 148, 158)
COLOR_GLASS_BG = (14, 20, 32, 220)

# ==============================================================================
# 3. BASE DE DADOS DE TECNOLOGIAS E STACKS
# ==============================================================================
TECH_DATA = [
    {"name": "HTML5", "tag": "<html>", "color": (228, 77, 38), "glow": (255, 100, 50)},
    {"name": "CSS3", "tag": ".style {}", "color": (38, 77, 228), "glow": (80, 120, 255)},
    {"name": "JavaScript", "tag": "const dev =", "color": (247, 223, 30), "glow": (255, 240, 100)},
    {"name": "React", "tag": "<JSX />", "color": (97, 218, 251), "glow": (150, 235, 255)},
    {"name": "Node.js", "tag": "npm start", "color": (104, 160, 99), "glow": (140, 210, 130)},
    {"name": "Python", "tag": "def main():", "color": (55, 118, 171), "glow": (255, 212, 59)},
    {"name": "Docker", "tag": "docker run", "color": (36, 150, 237), "glow": (100, 190, 255)},
    {"name": "TypeScript", "tag": "type Dev =", "color": (49, 120, 198), "glow": (100, 160, 240)},
    {"name": "SQL", "tag": "SELECT *", "color": (234, 140, 0), "glow": (255, 180, 50)},
    {"name": "Git", "tag": "git commit", "color": (240, 80, 51), "glow": (255, 120, 90)},
]

# ==============================================================================
# 4. CARREGAMENTO E GERENCIAMENTO DE FONTES
# ==============================================================================
class FontManager:
    def __init__(self):
        self.title = pygame.font.SysFont("Trebuchet MS", 54, bold=True)
        self.subtitle = pygame.font.SysFont("Trebuchet MS", 18)
        self.card = pygame.font.SysFont("Consolas", 18, bold=True)
        self.hud = pygame.font.SysFont("Consolas", 17, bold=True)
        self.btn = pygame.font.SysFont("Trebuchet MS", 18, bold=True)
        self.tag = pygame.font.SysFont("Consolas", 12)
        self.code = pygame.font.SysFont("Consolas", 11)

fonts = FontManager()

# ==============================================================================
# 5. GERENCIADOR DE ÁUDIO SINTETIZADO PROCEDURAL
# ==============================================================================
class SoundManager:
    @staticmethod
    def play_cut_sound():
        try:
            sample_rate = 22050
            duration = 0.04
            n_samples = int(sample_rate * duration)
            buf = bytearray()
            for i in range(n_samples):
                val = int(127 + 127 * math.sin(i * 0.18) * (1 - i / n_samples))
                buf.append(val)
            sound = pygame.mixer.Sound(buffer=bytes(buf))
            sound.set_volume(0.25)
            sound.play()
        except Exception:
            pass

    @staticmethod
    def play_bug_sound():
        try:
            sample_rate = 22050
            duration = 0.1
            n_samples = int(sample_rate * duration)
            buf = bytearray()
            for i in range(n_samples):
                val = int(127 + 127 * math.sin(i * 0.05) * (1 - i / n_samples))
                buf.append(val)
            sound = pygame.mixer.Sound(buffer=bytes(buf))
            sound.set_volume(0.35)
            sound.play()
        except Exception:
            pass

# ==============================================================================
# 6. MOTOR MATEMÁTICO 3D (ÁLGEBRA LINEAR & VETORES)
# ==============================================================================
class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def rotate_x(self, angle):
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        return Vector3D(self.x, self.y * cos_a - self.z * sin_a, self.y * sin_a + self.z * cos_a)

    def rotate_y(self, angle):
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        return Vector3D(self.x * cos_a + self.z * sin_a, self.y, -self.x * sin_a + self.z * cos_a)

    def rotate_z(self, angle):
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        return Vector3D(self.x * cos_a - self.y * sin_a, self.x * sin_a + self.y * cos_a, self.z)

    def project(self, fov=400, distance=500):
        factor = fov / (distance + self.z) if (distance + self.z) != 0 else 1
        x_proj = self.x * factor + WIDTH / 2
        y_proj = -self.y * factor + HEIGHT / 2
        return x_proj, y_proj, factor

# ==============================================================================
# 7. SISTEMA DE PARTÍCULAS E FAÍSCAS (BURST ENGINE)
# ==============================================================================
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.uniform(2.5, 5.5)
        self.vx = random.uniform(-7, 7)
        self.vy = random.uniform(-7, 7)
        self.gravity = 0.15
        self.life = 1.0
        self.decay = random.uniform(0.025, 0.05)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.size = max(0, self.size - 0.06)
        self.life -= self.decay

    def draw(self, surface):
        if self.life > 0 and self.size > 0:
            alpha = int(self.life * 255)
            p_surf = pygame.Surface((int(self.size * 2), int(self.size * 2)), pygame.SRCALPHA)
            pygame.draw.circle(p_surf, (*self.color, alpha), (int(self.size), int(self.size)), int(self.size))
            surface.blit(p_surf, (self.x - self.size, self.y - self.size))

# ==============================================================================
# 8. FRAGMENTO DE CARD FATIADO (FÍSICA DE CORTE REAL)
# ==============================================================================
class Piece3D:
    def __init__(self, x, y, z, w, h, d, color, vx, angle):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.d = d
        self.color = color
        self.vx = vx
        self.vy = random.uniform(4, 8)
        self.vz = random.uniform(-2, 2)
        self.gravity = 0.5
        self.rot_x = random.uniform(0, 360)
        self.rot_y = random.uniform(0, 360)
        self.v_rot = random.uniform(-8, 8)
        self.active = True

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy -= self.gravity
        self.rot_x += self.v_rot
        self.rot_y += self.v_rot
        if self.y < -500:
            self.active = False

    def draw(self, surface):
        v = Vector3D(self.x, self.y, self.z)
        px, py, factor = v.project()
        w_proj = int(self.w * factor)
        h_proj = int(self.h * factor)
        
        surf = pygame.Surface((max(1, w_proj), max(1, h_proj)), pygame.SRCALPHA)
        pygame.draw.rect(surf, (*self.color, 200), (0, 0, w_proj, h_proj), border_radius=6)
        pygame.draw.rect(surf, COLOR_WHITE, (0, 0, w_proj, h_proj), 1, border_radius=6)
        
        rot_s = pygame.transform.rotate(surf, self.rot_x)
        surface.blit(rot_s, (px - rot_s.get_width() // 2, py - rot_s.get_height() // 2))

# ==============================================================================
# 9. CARDS 3D (PRISMAS VOLUMÉTRICOS COM ILUMINAÇÃO)
# ==============================================================================
class TechCard3D:
    def __init__(self, speed_mult=1.0, bug_chance=0.20):
        self.is_bug = random.random() < bug_chance
        if self.is_bug:
            self.name = "BUG!"
            self.tag = "CRITICAL ERROR"
            self.color = (220, 20, 50)
            self.glow = (255, 60, 90)
        else:
            data = random.choice(TECH_DATA)
            self.name = data["name"]
            self.tag = data["tag"]
            self.color = data["color"]
            self.glow = data["glow"]

        self.w, self.h, self.d = 135, 72, 36

        self.x = random.randint(-260, 260)
        self.y = -360
        self.z = random.randint(-50, 50)

        self.vx = random.uniform(-2.5, 2.5)
        self.vy = random.uniform(16.5, 21.5) * speed_mult
        self.vz = random.uniform(-1, 1)
        self.gravity = 0.42

        self.rot_x = random.uniform(0, 360)
        self.rot_y = random.uniform(0, 360)
        self.rot_z = random.uniform(0, 360)

        self.v_rot_x = random.uniform(-3, 3)
        self.v_rot_y = random.uniform(-4, 4)
        self.v_rot_z = random.uniform(-2, 2)

        self.sliced = False
        self.active = True

        self.vertices = [
            Vector3D(-self.w/2, -self.h/2, -self.d/2),
            Vector3D( self.w/2, -self.h/2, -self.d/2),
            Vector3D( self.w/2,  self.h/2, -self.d/2),
            Vector3D(-self.w/2,  self.h/2, -self.d/2),
            Vector3D(-self.w/2, -self.h/2,  self.d/2),
            Vector3D( self.w/2, -self.h/2,  self.d/2),
            Vector3D( self.w/2,  self.h/2,  self.d/2),
            Vector3D(-self.w/2,  self.h/2,  self.d/2),
        ]

        self.faces = [
            ([0, 1, 2, 3], (0, 0, -1)),
            ([5, 4, 7, 6], (0, 0, 1)),
            ([4, 0, 3, 7], (-1, 0, 0)),
            ([1, 5, 6, 2], (1, 0, 0)),
            ([4, 5, 1, 0], (0, -1, 0)),
            ([3, 2, 6, 7], (0, 1, 0)),
        ]

        self.screen_x = 0
        self.screen_y = 0

    def update(self):
        if not self.sliced:
            self.x += self.vx
            self.y += self.vy
            self.z += self.vz
            self.vy -= self.gravity

            self.rot_x += self.v_rot_x
            self.rot_y += self.v_rot_y
            self.rot_z += self.v_rot_z

            if self.y < -450:
                self.active = False

    def draw(self, surface):
        if not self.sliced:
            transformed_vertices = []
            for v in self.vertices:
                r_v = v.rotate_x(self.rot_x).rotate_y(self.rot_y).rotate_z(self.rot_z)
                world_v = Vector3D(r_v.x + self.x, r_v.y + self.y, r_v.z + self.z)
                transformed_vertices.append(world_v)

            center_v = Vector3D(self.x, self.y, self.z)
            cx, cy, _ = center_v.project()
            self.screen_x, self.screen_y = cx, cy

            rendered_faces = []
            for face_indices, normal_dir in self.faces:
                pts = []
                avg_z = 0
                for idx in face_indices:
                    pv = transformed_vertices[idx]
                    px, py, _ = pv.project()
                    pts.append((px, py))
                    avg_z += pv.z

                avg_z /= len(face_indices)

                norm_v = Vector3D(*normal_dir).rotate_x(self.rot_x).rotate_y(self.rot_y).rotate_z(self.rot_z)
                light_dir = Vector3D(0.5, 0.8, -1)
                dot = max(0.25, (norm_v.x * light_dir.x + norm_v.y * light_dir.y + norm_v.z * light_dir.z) / 2)

                face_color = (
                    min(255, int(self.color[0] * dot + 20)),
                    min(255, int(self.color[1] * dot + 20)),
                    min(255, int(self.color[2] * dot + 20))
                )

                rendered_faces.append((avg_z, pts, face_color))

            rendered_faces.sort(key=lambda item: item[0])

            for avg_z, pts, face_color in rendered_faces:
                pygame.draw.polygon(surface, face_color, pts)
                pygame.draw.polygon(surface, COLOR_WHITE, pts, 1)

            txt_surf = fonts.card.render(self.name, True, COLOR_WHITE)
            surface.blit(txt_surf, (cx - txt_surf.get_width() // 2, cy - 10))

    def check_slice(self, pos1, pos2):
        if self.sliced or not self.active:
            return False

        dist = math.hypot(self.screen_x - pos2[0], self.screen_y - pos2[1])
        if dist < 65:
            self.sliced = True
            if self.is_bug:
                SoundManager.play_bug_sound()
            else:
                SoundManager.play_cut_sound()
            return True
        return False

# ==============================================================================
# 10. MAPA 1: CYBER MATRIX 3D (ESPAÇO E PERSPECTIVA)
# ==============================================================================
class SpaceGrid3D:
    def __init__(self):
        self.stars = [Vector3D(random.randint(-650, 650), random.randint(-450, 450), random.randint(10, 450)) for _ in range(160)]

    def draw(self, surface):
        surface.fill(COLOR_BG_DARK)

        for star in self.stars:
            star.z -= 1.8
            if star.z <= 1:
                star.z = 450

            px, py, factor = star.project()
            size = max(1, int(3.5 * factor))
            if 0 <= px <= WIDTH and 0 <= py <= HEIGHT:
                color_val = min(255, int(170 * factor))
                pygame.draw.circle(surface, (color_val, color_val, color_val), (int(px), int(py)), size)

# ==============================================================================
# 11. MAPA 2: VS CODE IDE DARK MODE
# ==============================================================================
class VSCodeMap:
    def __init__(self):
        self.code_lines = [
            "import os, sys",
            "from engine import Matrix3D",
            "",
            "class DevNinjaEngine:",
            "    def __init__(self):",
            "        self.status = 'READY'",
            "        self.stack = ['Python', 'JS', 'React']",
            "",
            "    def execute_deploy(self):",
            "        print('Deploying to production...')",
            "        return True",
            "",
            "# System Initialized",
            "if __name__ == '__main__':",
            "    app = DevNinjaEngine()",
            "    app.execute_deploy()"
        ]

    def draw(self, surface):
        surface.fill(COLOR_BG_VSCODE)
        
        # Barra lateral estilo VS Code
        pygame.draw.rect(surface, COLOR_VSCODE_SIDEBAR, (0, 0, 50, HEIGHT))
        pygame.draw.rect(surface, COLOR_VSCODE_TAB, (50, 0, WIDTH - 50, 38))

        tabs = ["app.py", "styles.css", "main.js"]
        for i, tab in enumerate(tabs):
            bg_col = COLOR_VSCODE_TAB_ACTIVE if i == 0 else COLOR_VSCODE_TAB
            rect = pygame.Rect(50 + i * 140, 0, 138, 38)
            pygame.draw.rect(surface, bg_col, rect)
            txt = fonts.tag.render(tab, True, COLOR_WHITE if i == 0 else COLOR_MUTED)
            surface.blit(txt, (65 + i * 140, 11))

        # Renderizar linhas de código no fundo
        for idx, line in enumerate(self.code_lines):
            num_txt = fonts.code.render(str(idx + 1).rjust(2), True, (90, 90, 90))
            code_txt = fonts.code.render(line, True, (160, 175, 195))
            surface.blit(num_txt, (60, 50 + idx * 26))
            surface.blit(code_txt, (95, 50 + idx * 26))

# ==============================================================================
# 12. COMPONENTES DE INTERFACE GLASSMORPHIC (UI SYSTEM)
# ==============================================================================
class UIComponents:
    @staticmethod
    def draw_glass_rect(surface, rect, color_bg, color_border, border_w=1, radius=16):
        glass_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(glass_surf, color_bg, (0, 0, rect.width, rect.height), border_radius=radius)
        surface.blit(glass_surf, rect.topleft)
        pygame.draw.rect(surface, color_border, rect, border_w, border_radius=radius)

    @staticmethod
    def draw_coffee_cup(surface, x, y, active=True, steam_timer=0.0):
        color_cup = COLOR_WHITE if active else COLOR_GRAY
        color_coffee = (180, 100, 40) if active else (50, 50, 50)
        
        pygame.draw.ellipse(surface, color_cup, (x - 2, y + 16, 28, 6))
        pygame.draw.rect(surface, color_cup, (x, y + 4, 24, 14), border_bottom_left_radius=6, border_bottom_right_radius=6)
        pygame.draw.ellipse(surface, color_coffee, (x + 2, y + 2, 20, 6))
        pygame.draw.arc(surface, color_cup, (x + 20, y + 5, 10, 10), -1.5, 1.5, 3)

        if active:
            offset = math.sin(steam_timer) * 3
            pygame.draw.line(surface, (220, 220, 220), (x + 8 + offset, y - 4), (x + 8 - offset, y - 10), 2)
            pygame.draw.line(surface, (220, 220, 220), (x + 16 - offset, y - 4), (x + 16 + offset, y - 10), 2)

# ==============================================================================
# 13. ENGINE PRINCIPAL DO JOGO (GAME LOOP)
# ==============================================================================
class NinjaDevGame:
    def __init__(self):
        self.map_matrix = SpaceGrid3D()
        self.map_vscode = VSCodeMap()
        self.current_map = "MATRIX"  # MATRIX ou VSCODE
        self.state = "MENU"  # MENU, PLAYING, GAMEOVER
        self.difficulty = "PLENO"  # JUNIOR, PLENO, SENIOR
        
        self.steam_timer = 0.0
        self.particles = []
        self.pieces = []
        
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.cards = []
        self.spawn_timer = 0
        self.blade_trail = []
        self.sliced_count = 0
        self.total_spawned = 0
        self.combo = 0
        self.max_combo = 0
        self.particles.clear()
        self.pieces.clear()

    def get_difficulty_params(self):
        if self.difficulty == "JUNIOR": 
            return {"speed": 0.85, "interval": 65, "bug_chance": 0.12}
        elif self.difficulty == "SENIOR": 
            return {"speed": 1.15, "interval": 40, "bug_chance": 0.28}
        else: 
            return {"speed": 1.0, "interval": 50, "bug_chance": 0.20}

    def run(self):
        running = True
        while running:
            clock.tick(FPS)
            mouse_pos = pygame.mouse.get_pos()
            self.steam_timer += 0.10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.state == "MENU":
                        if event.key == pygame.K_1: self.difficulty = "JUNIOR"
                        elif event.key == pygame.K_2: self.difficulty = "PLENO"
                        elif event.key == pygame.K_3: self.difficulty = "SENIOR"
                        elif event.key == pygame.K_m:
                            self.current_map = "VSCODE" if self.current_map == "MATRIX" else "MATRIX"
                        elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                            self.reset_game()
                            self.state = "PLAYING"
                    elif self.state == "GAMEOVER":
                        if event.key == pygame.K_r:
                            self.reset_game()
                            self.state = "PLAYING"
                        elif event.key == pygame.K_m:
                            self.state = "MENU"

                elif event.type == pygame.MOUSEBUTTONDOWN and self.state == "MENU":
                    start_btn = pygame.Rect(WIDTH // 2 - 200, 520, 400, 65)
                    if start_btn.collidepoint(mouse_pos):
                        self.reset_game()
                        self.state = "PLAYING"

            # Renderização de Fundo Dinâmico
            if self.current_map == "MATRIX": 
                self.map_matrix.draw(screen)
            else: 
                self.map_vscode.draw(screen)

            # Controle de Estado do Jogo
            if self.state == "MENU":
                self.draw_menu(mouse_pos)
            elif self.state == "PLAYING":
                self.update_playing(mouse_pos)
                self.draw_playing()
            elif self.state == "GAMEOVER":
                self.draw_gameover()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def draw_menu(self, mouse_pos):
        header_rect = pygame.Rect(WIDTH // 2 - 360, 100, 720, 120)
        UIComponents.draw_glass_rect(screen, header_rect, COLOR_GLASS_BG, COLOR_CYAN, border_w=2, radius=20)

        title = fonts.title.render("NINJA DEV 3D", True, COLOR_CYAN)
        sub = fonts.subtitle.render("> Direct Matrix Engine & Real-Time Physics System", True, COLOR_MUTED)
        
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 115))
        screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, 175))

        # Botão Seletor de Mapa
        map_btn = pygame.Rect(WIDTH // 2 - 160, 240, 320, 45)
        UIComponents.draw_glass_rect(screen, map_btn, (20, 28, 42, 220), COLOR_CYAN, border_w=1, radius=10)
        map_txt = fonts.btn.render(f"MAPA ATIVO [ M ]: {self.current_map}", True, COLOR_CYAN)
        screen.blit(map_txt, (WIDTH // 2 - map_txt.get_width() // 2, 250))

        # Cards Seletor de Dificuldade
        levels = [
            ("1. JÚNIOR", "JUNIOR", COLOR_GREEN, "Velocidade -15%"),
            ("2. PLENO", "PLENO", COLOR_GOLD, "Modo Padrão"),
            ("3. SÊNIOR", "SENIOR", COLOR_RED, "Bugs +30%")
        ]

        card_w, card_h = 220, 100
        total_w = len(levels) * card_w + (len(levels) - 1) * 20
        start_x = WIDTH // 2 - total_w // 2

        for i, (label, key, color, desc) in enumerate(levels):
            x = start_x + i * (card_w + 20)
            y = 310
            box_rect = pygame.Rect(x, y, card_w, card_h)
            
            is_selected = self.difficulty == key
            card_border = color if is_selected else COLOR_GRAY
            card_bg = (24, 34, 54, 230) if is_selected else (14, 18, 28, 190)

            UIComponents.draw_glass_rect(screen, box_rect, card_bg, card_border, border_w=2 if is_selected else 1, radius=16)

            txt_color = color if is_selected else COLOR_MUTED
            txt = fonts.btn.render(label, True, txt_color)
            desc_txt = fonts.tag.render(desc, True, COLOR_MUTED)
            
            screen.blit(txt, (x + card_w // 2 - txt.get_width() // 2, y + 25))
            screen.blit(desc_txt, (x + card_w // 2 - desc_txt.get_width() // 2, y + 60))

        # Botão Principal "INICIAR DEPLOY"
        start_btn = pygame.Rect(WIDTH // 2 - 200, 520, 400, 65)
        is_hover = start_btn.collidepoint(mouse_pos)
        btn_bg = COLOR_CYAN if not is_hover else (100, 245, 255)
        
        shadow_rect = pygame.Rect(WIDTH // 2 - 196, 524, 400, 65)
        pygame.draw.rect(screen, (0, 80, 110), shadow_rect, border_radius=16)
        
        pygame.draw.rect(screen, btn_bg, start_btn, border_radius=16)
        pygame.draw.rect(screen, COLOR_WHITE if is_hover else COLOR_CYAN, start_btn, 2, border_radius=16)
        
        btn_txt = fonts.btn.render("INICIAR DEPLOY  [ ENTER ]", True, COLOR_BG_DARK)
        screen.blit(btn_txt, (WIDTH // 2 - btn_txt.get_width() // 2, 540))

    def update_playing(self, mouse_pos):
        params = self.get_difficulty_params()

        if pygame.mouse.get_pressed()[0] or len(self.blade_trail) > 0:
            self.blade_trail.append(mouse_pos)
            if len(self.blade_trail) > 12:
                self.blade_trail.pop(0)

        self.spawn_timer += 1
        if self.spawn_timer > params["interval"]:
            self.spawn_timer = 0
            self.cards.append(TechCard3D(speed_mult=params["speed"], bug_chance=params["bug_chance"]))
            self.total_spawned += 1

        if len(self.blade_trail) >= 2:
            p1 = self.blade_trail[-2]
            p2 = self.blade_trail[-1]
            for card in self.cards:
                if card.check_slice(p1, p2):
                    # Criar partículas
                    for _ in range(22):
                        self.particles.append(Particle(card.screen_x, card.screen_y, card.color))
                    
                    # Criar fragmentos físicos 3D
                    self.pieces.append(Piece3D(card.x, card.y, card.z, card.w//2, card.h, card.d, card.color, -4, card.rot_x))
                    self.pieces.append(Piece3D(card.x, card.y, card.z, card.w//2, card.h, card.d, card.color, 4, card.rot_x))

                    if card.is_bug:
                        self.lives -= 1
                        self.combo = 0
                        if self.lives <= 0: self.state = "GAMEOVER"
                    else:
                        self.score += 100
                        self.sliced_count += 1
                        self.combo += 1
                        if self.combo > self.max_combo: self.max_combo = self.combo

        # Atualizar partículas e fragmentos
        for p in self.particles: p.update()
        self.particles = [p for p in self.particles if p.life > 0]

        for piece in self.pieces: piece.update()
        self.pieces = [p for p in self.pieces if p.active]

        for card in self.cards:
            card.update()
            if not card.sliced and card.y < -400 and not card.is_bug:
                card.active = False
                self.lives -= 1
                self.combo = 0
                if self.lives <= 0: self.state = "GAMEOVER"

        self.cards = [c for c in self.cards if c.active]

    def draw_playing(self):
        for card in self.cards: card.draw(screen)
        for piece in self.pieces: piece.draw(screen)
        for p in self.particles: p.draw(screen)

        # Rastro da Lâmina Neon
        if len(self.blade_trail) > 1:
            pygame.draw.lines(screen, COLOR_CYAN, False, self.blade_trail, 6)
            pygame.draw.lines(screen, COLOR_WHITE, False, self.blade_trail, 2)

        # HUD Topo Clean
        hud_rect = pygame.Rect(0, 0, WIDTH, 65)
        UIComponents.draw_glass_rect(screen, hud_rect, (12, 16, 26, 220), COLOR_CYAN, border_w=1, radius=0)

        score_txt = fonts.hud.render(f"SCORE: {self.score}", True, COLOR_CYAN)
        combo_txt = fonts.hud.render(f"COMBO: {self.combo}x", True, COLOR_GOLD if self.combo > 1 else COLOR_MUTED)
        level_txt = fonts.hud.render(f"NÍVEL: {self.difficulty}", True, COLOR_WHITE)

        screen.blit(score_txt, (30, 22))
        screen.blit(combo_txt, (200, 22))
        screen.blit(level_txt, (WIDTH // 2 - level_txt.get_width() // 2, 22))

        cafe_label = fonts.hud.render("CAFÉS:", True, COLOR_RED)
        screen.blit(cafe_label, (WIDTH - 240, 22))

        for l in range(3):
            UIComponents.draw_coffee_cup(screen, WIDTH - 140 + l * 38, 20, active=(l < self.lives), steam_timer=self.steam_timer)

    def draw_gameover(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((10, 14, 23, 235))
        screen.blit(overlay, (0, 0))

        card_w, card_h = 540, 440
        card_rect = pygame.Rect(WIDTH // 2 - card_w // 2, HEIGHT // 2 - card_h // 2, card_w, card_h)
        
        UIComponents.draw_glass_rect(screen, card_rect, COLOR_GLASS_BG, COLOR_RED, border_w=2, radius=18)

        title = fonts.title.render("SYSTEM CRASH!", True, COLOR_RED)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 180))

        rank = "Senior Tech Lead 🚀" if self.score > 3000 else ("Full-Stack Engineer 💻" if self.score > 1500 else "Junior Bug Hunter 🐛")
        acc = int((self.sliced_count / max(1, self.total_spawned)) * 100)

        stats = [
            ("Pontuação Final:", f"{self.score} pts"),
            ("Classificação Dev:", rank),
            ("Precisão de Corte:", f"{acc}%"),
            ("Maior Combo:", f"{self.max_combo}x"),
            ("Dificuldade:", self.difficulty)
        ]

        for i, (label, val) in enumerate(stats):
            y_pos = HEIGHT // 2 - 90 + i * 38
            lbl_surf = fonts.hud.render(label, True, COLOR_MUTED)
            val_surf = fonts.hud.render(val, True, COLOR_WHITE if i != 1 else COLOR_GOLD)
            
            screen.blit(lbl_surf, (WIDTH // 2 - 200, y_pos))
            screen.blit(val_surf, (WIDTH // 2 + 30, y_pos))

        r_txt = fonts.btn.render("[ R ] REINICIAR   |   [ M ] MENU", True, COLOR_GREEN)
        screen.blit(r_txt, (WIDTH // 2 - r_txt.get_width() // 2, HEIGHT // 2 + 140))

# ==============================================================================
# 14. PONTO DE ENTRADA DA APLICAÇÃO
# ==============================================================================
if __name__ == "__main__":
    game = NinjaDevGame()
    game.run()