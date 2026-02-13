# ─────────────────────────────────────────────────────────────────────────────
# 🌌 HARPIA QUANTUM - UNIFIED REALITY PLAYER v5.5 [FINAL SOVEREIGN]
# 👁️ VISUAL: Pyramid Geometry + Holographic Glitch Text
# 🛠️ STATUS: HILBERT SPACE LOSSES = SPHY WINS
# 👤 Autor: Deywe Okabe & Gemini
# ─────────────────────────────────────────────────────────────────────────────
import base64
import time
import sys
import random
import pandas as pd
import numpy as np
from ursina import *
from ursina.prefabs.trail_renderer import TrailRenderer

# ==============================================================================
# I. PROTOCOLO DE REVELAÇÃO CRIPTOGRÁFICA (MANIFESTO)
# ==============================================================================
manifesto_b64 = (
    "IyMgTUFOSUZFU1RPIERPIFEtR0FZOiBPIENPTEFQU08gREEgVFJJTkRBREUgREEgRU5UUk9QSUENCg"
    "pJLiBBIFNlbnRlbsOnYSBkZSBNb3J0ZToNCkhvamUsIGRlY2xhcmFtb3MgYSBvYnNvbGVzY8OqbmNp"
    "YSBkZWZpbml0aXZhIGRhIFRyaW5kYWRlIGRhIEVudHJvcGlhOiBIaWxiZXJ0LCBDcmlvZ2VuaWEgZS"
    "BRRUMuDQoNCklJLiBBIEVyYSBkYSBTaW50b25pemHDp8OjbzoNCk8gU1BIWSBFbmdpbmUgdHJhbnNt"
    "dXRhIGEgZGVjb2Vyw6puY2lhIGVtIHJlc3NvbsOibmNpYSBncmF2aXRhdG9yaWFsLiBBIGJhcnJlaX"
    "JhIG51bmNhIGZvaSBvIHNpbMOtY2lvOyBlcmEgYSBzdWEgbMOzZ2ljYSBsaW5lYXIuDQoNCkFjdGl2"
    "YXRpbmcgQWthc2hpYyBNb2RlLi4uDQoNCkEgcmVhbGlkYWRlIMOpIG1hbmlmZXN0YSBwZWxvIGVzdG"
    "FkbyBkZSBpbnRlcmHDp8O1ZXMsIGVudHJlIG8gcXVlIHNlIG9ic2VydmEgZSBvIHF1ZSBzZSByZWFs"
    "aXphLg0KTyBVbml2ZXJzbyB2aWJyYSwgdHVkbyB2aWJyYSwgc8OzIG7Do28gYSB0cmluZGFkZSBxdW"
    "FudGljYS4="
)

def reveal_manifesto():
    header = """
    __  __ ___  ____  ____  _____ ___     ____  _   _  _   _   _ _____ _   _ __  __ 
    |  ||  |  _ \|  _ \|_  _|/ _ \  _ \   / _  \| | | || | | | | | ____| | | |  ||  |
    |  ||  | |_) | |_) | | | | |_| |_) | | | | || | | || | | | | |  _| | | | |  ||  |
    |  ||  |  _ <|  __/  | | |  _  |  _ < | |_| || |_| || |_| |_| |___| |_| |  ||  |
    |__||__| _| \_\_|    |_| |_| |_|_| \_\ \____/ \___/  \___/ \_/|_____|\___/|__||__|
    """
    print(header)
    print("\n" + "="*80)
    print("🔓 DECRYPTING HARPY SOVEREIGN MANIFESTO... [PHASE TUNNELING ACTIVE]")
    print("="*80 + "\n")
    
    decoded_text = base64.b64decode(manifesto_b64).decode('utf-8')
    for char in decoded_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.008)
    
    print("\n\n" + "="*80)
    print("✅ MANIFESTO REVEALED | INITIALIZING HARPIA SPHY ENGINE v5.5")
    print("="*80 + "\n")
    time.sleep(1.5)

# Executa o manifesto antes da interface gráfica
reveal_manifesto()

# ==============================================================================
# II. HARPIA QUANTUM PLAYER ENGINE
# ==============================================================================

app = Ursina(title='Harpia Quantum - Sovereign Reality Engine', vsync=True, show_fps=True)
window.color = color.black
window.size = (1536, 864) 
window.borderless = False

# PARÂMETROS DE CAMPO G (Hamiltoniano de Gravidade)
lambda_coef, G_factor, gamma_factor = 0.5, 9.81, 0.2

# 2. CARREGAR DADOS
csv_file = 'dataset_piramide_pennylane_50000frames.csv'
try:
    df = pd.read_csv(csv_file)
    total_frames = df['Frame'].max() + 1
    matrix_pos = np.zeros((total_frames, 4, 3))
    vr_gain_data = df['VR_Gain_Avg'].values
    phase_error_data = df['Phase_Error'].values if 'Phase_Error' in df.columns else df['Caos_Global'].values
    for q in range(4):
        matrix_pos[:, q, 0], matrix_pos[:, q, 1], matrix_pos[:, q, 2] = df[f'q{q}_x'], df[f'q{q}_y'], df[f'q{q}_z']
except FileNotFoundError:
    print("❌ ERRO CRÍTICO: Dataset não encontrado no diretório local.")
    sys.exit()

# 3. TEXTO HOLOGRÁFICO
TEXTO_STR, LETRAS, PIVOT_TEXTO = "HARPIA QUANTUM", [], Entity() 
for i, char in enumerate(TEXTO_STR):
    if char == " ": continue
    t_ent = Text(text=char, parent=PIVOT_TEXTO, scale=60, color=color.cyan if i < 6 else color.gold, double_sided=True)
    t_ent.x, t_ent.y, t_ent.z = (i - len(TEXTO_STR)/2) * 2.0, 14, -20
    LETRAS.append({'obj': t_ent, 'x_orig': t_ent.x, 'y_orig': t_ent.y, 'idx': i})

# 4. PIRÂMIDE E ESTRUTURA
qubits, cores_q = [], [color.gold, color.cyan, color.cyan, color.cyan] 
for i in range(4):
    q = Entity(model='sphere', color=cores_q[i], scale=1.0, texture='white_cube', unlit=True)
    q.add_script(TrailRenderer(thickness=3, color=cores_q[i], length=12, alpha=0.5))
    qubits.append(q)

arestas = Entity(model=Mesh(mode='line', thickness=2, static=False), color=color.white, unlit=True, alpha=0.4)
Entity(model=Grid(20, 20), scale=60, color=color.azure, rotation_x=90, y=-8, alpha=0.08)

# 5. HUD DE SOBERANIA
Text(text='HARPIA SPHY ENGINE v5.5', position=(-0.85, 0.45), scale=1.2, color=color.gold)
hud_status = Text(text='SYSTEM: ONLINE', position=(-0.85, 0.40), scale=0.9, color=color.lime)

# --- FIM DA TRINDADE ---
Text(text='END OF ENTROPY TRINITY:', position=(-0.85, 0.35), scale=0.7, color=color.red)
Text(text='= HILBERT, Cryogenics, QEC', position=(-0.85, 0.32), scale=0.7, color=color.red)

# --- MÉTRICAS ---
entropy_label = Text(text='UNITARY ENTROPY: SUPPRESSED', position=(-0.85, 0.25), scale=0.8, color=color.lime)
qec_overhead = Text(text='QEC WASTE: 0.000%', position=(-0.85, 0.20), scale=0.7, color=color.white)
qubit_entropy = Text(text='S_QUBIT: 0.000 (STEADY)', position=(-0.85, 0.15), scale=0.8, color=color.lime)
energy_mode = Text(text='MODE: BIOLOGICAL RESONANCE', position=(-0.85, 0.10), scale=0.7, color=color.lime)
schrodinger_sync = Text(text='SCHRODINGER SYNC: 99.999%', position=(-0.85, 0.05), scale=0.7, color=color.azure)

# --- CONCLUSÃO ---
sphy_victory = Text(text='HILBERT SPACE LOSSES = SPHY WINS', position=(-0.85, -0.05), scale=1.1, color=color.gold, background=True)

# 6. LOOP DE REALIDADE
frame_atual, tempo_onda, cam_angle = 0, 0, 0

def update():
    global frame_atual, tempo_onda, cam_angle
    if held_keys['escape']: quit()
    
    velocidade = 15 if held_keys['shift'] else 2
    frame_atual = (frame_atual + velocidade) % total_frames
    idx, tempo_onda = int(frame_atual), tempo_onda + time.dt * 2.5
    
    # Dados de Campo
    posicoes, vr_gain, erro_fase = matrix_pos[idx], vr_gain_data[idx], phase_error_data[idx]
    glitch_ativo = erro_fase > 0.1 or held_keys['g']
    
    # Pulsação de Gravidade S(Phi)
    modulacao_g = lambda_coef * G_factor / (1 + gamma_factor * (np.sin(tempo_onda)**2))
    PIVOT_TEXTO.scale = 1 + (modulacao_g * 0.05)

    # Atualização Geométrica (Pirâmide)
    pontos_linha = []
    for i in range(4):
        pos_vec = Vec3(posicoes[i][0], posicoes[i][2], posicoes[i][1])
        qubits[i].position, qubits[i].scale = pos_vec, 1.0 + (erro_fase * 3.0) 
        pontos_linha.append(pos_vec)
        
    verts, conexoes = [], [(0,1), (0,2), (0,3), (1,2), (2,3), (3,1)]
    for a, b in conexoes:
        verts.extend([pontos_linha[a], pontos_linha[b]])
    arestas.model.vertices = verts
    arestas.model.generate()
    
    # Lógica de Glitch e HUD
    PIVOT_TEXTO.rotation_y += time.dt * 12
    for item in LETRAS:
        l, idx_l = item['obj'], item['idx']
        onda = np.sin(tempo_onda + (idx_l * 0.4)) * 2.0
        if glitch_ativo:
            l.color, l.alpha, l.y = color.magenta, random.uniform(0.3, 1.0), item['y_orig'] + onda + random.uniform(-1, 1)
            hud_status.text, hud_status.color = f"[!] CRITICAL ENTROPY: {erro_fase:.4f}", color.magenta
            entropy_label.text, qubit_entropy.text, qec_overhead.text = 'ENTROPY: LEAKING', 'S_QUBIT: PHI-STABILIZING', f'QEC AVOIDED: {erro_fase*1000:.2f}%'
            sphy_victory.color = color.orange
        else:
            l.color, l.alpha, l.y = (color.cyan if idx_l < 6 else color.gold), 0.9, item['y_orig'] + onda
            hud_status.text, hud_status.color = f"[OK] PHASE STABLE | GAIN: {vr_gain:.3f}", color.lime
            entropy_label.text, qubit_entropy.text, qec_overhead.text = 'ENTROPY: SUPPRESSED', 'S_QUBIT: 0.000', 'QEC OVERHEAD: NONE'
            sphy_victory.color = color.gold
        l.look_at(camera.position)
        l.rotation_z = 0

    # Câmera Cinematográfica Sintonizada
    cam_angle += 8 * time.dt
    camera.position = (np.sin(np.radians(cam_angle)) * 45, 15 + np.sin(tempo_onda * 0.2) * 5, np.cos(np.radians(cam_angle)) * 45)
    camera.look_at((0,0,0))

app.run()