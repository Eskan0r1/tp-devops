import subprocess
import sys

version = sys.argv[1] if len(sys.argv) > 1 else "latest"
port = sys.argv[2] if len(sys.argv) > 2 else "5000"

container_name = "devops-web"
image_name = f"devops-app:{version}"

try:
    print(f"Déploiement version {version} sur le port {port}...")

    # Stop & remove ancien container
    subprocess.run(f"docker stop {container_name} || true", shell=True)
    subprocess.run(f"docker rm {container_name} || true", shell=True)

    # Build image
    result = subprocess.run(f"docker build -t {image_name} .", shell=True)
    if result.returncode != 0:
        print("Erreur lors du build ! Rollback effectué")
        sys.exit(1)

    # Run container
    subprocess.run(f"docker run -d -p {port}:5000 --name {container_name} {image_name}", shell=True)

    print(f"App déployée sur localhost:{port} (version {version})")

except Exception as e:
    print(f"Erreur déploiement: {e}")
