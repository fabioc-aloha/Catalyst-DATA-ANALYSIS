#!/usr/bin/env python3
"""
Requirements Validation Script
Checks for duplicates and inconsistencies across all requirements files.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

def parse_requirements_file(filepath: Path) -> Dict[str, str]:
    """Parse a requirements file and return package names with versions."""
    packages = {}
    if not filepath.exists():
        return packages
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Extract package name and version
            match = re.match(r'^([a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]|[a-zA-Z0-9])([><=!]+[^#]*)?', line)
            if match:
                package = match.group(1).lower()
                version = match.group(2) if match.group(2) else ""
                packages[package] = version.strip()
    
    return packages

def find_duplicates(all_packages: Dict[str, Dict[str, str]]) -> Dict[str, List[Tuple[str, str]]]:
    """Find packages that appear in multiple files."""
    package_files = {}
    
    for file, packages in all_packages.items():
        for package, version in packages.items():
            if package not in package_files:
                package_files[package] = []
            package_files[package].append((file, version))
    
    # Return only packages that appear in multiple files
    duplicates = {pkg: files for pkg, files in package_files.items() if len(files) > 1}
    return duplicates

def main():
    """Main validation function"""
    print("🔍 REQUIREMENTS FILES VALIDATION")
    print("==================================================")
    
    # Define requirements files to check
    files = [
        'requirements.txt',
        'requirements-analysis.txt', 
        'requirements-dev.txt',
        'requirements-SPSS.txt',
        'requirements-advanced.txt'
    ]
    
    # Parse all files
    all_packages = {}
    total_packages = 0
    
    for filepath in files:
        filepath_obj = Path(filepath)
        packages = parse_requirements_file(filepath_obj)
        all_packages[filepath] = packages
        print(f"📄 {filepath}: {len(packages)} packages")
        total_packages += len(packages)
    
    print(f"\n📊 Total packages across all files: {total_packages}")
    
    # Find duplicates
    duplicates = find_duplicates(all_packages)
    
    if duplicates:
        print(f"\n⚠️  DUPLICATES FOUND ({len(duplicates)} packages):")
        print("-" * 50)
        for package, files in duplicates.items():
            print(f"\n📦 {package}:")
            for file, version in files:
                print(f"   • {file}: {version}")
    else:
        print("\n✅ NO DUPLICATES FOUND!")
    
    # Calculate unique packages
    unique_packages = set()
    for packages in all_packages.values():
        unique_packages.update(packages.keys())
    
    print(f"\n📈 SUMMARY:")
    print(f"   • Total unique packages: {len(unique_packages)}")
    print(f"   • Total package entries: {total_packages}")
    print(f"   • Duplicate entries: {total_packages - len(unique_packages)}")
    print(f"   • Efficiency: {len(unique_packages)/total_packages*100:.1f}%")
    
    if not duplicates:
        print("\n🎉 Requirements files are properly organized!")
        return 0
    else:
        print(f"\n❌ Found {len(duplicates)} duplicate packages that need attention.")
        return 1

if __name__ == "__main__":
    exit(main())
