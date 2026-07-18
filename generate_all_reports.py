"""
Master Results Report Generator
Generates both console tables and HTML report for training results
"""

import subprocess
import sys
import os


def main():
    """Run all report generation scripts."""
    print("\n" + "="*80)
    print(" "*15 + "EMOTION RECOGNITION - COMPREHENSIVE RESULTS REPORT GENERATOR")
    print("="*80 + "\n")
    
    # Try to generate HTML report first (no external dependencies)
    print("📄 Generating HTML Report...")
    try:
        result = subprocess.run([sys.executable, 'generate_html_report.py'], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(result.stdout)
            print("✓ HTML report generated successfully!\n")
        else:
            print(f"⚠ Warning: {result.stderr}\n")
    except Exception as e:
        print(f"⚠ Could not generate HTML report: {e}\n")
    
    # Try to generate console tables (requires tabulate)
    print("📊 Generating Console Report with Tables...")
    try:
        result = subprocess.run([sys.executable, 'generate_results_report.py'], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(result.stdout)
            print("✓ Console report generated successfully!\n")
        else:
            if "No module named 'tabulate'" in result.stderr:
                print("⚠ tabulate module not installed. Installing...")
                os.system(f"{sys.executable} -m pip install tabulate -q")
                print("  Retrying...")
                result = subprocess.run([sys.executable, 'generate_results_report.py'], 
                                      capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    print(result.stdout)
                    print("✓ Console report generated successfully!\n")
                else:
                    print(f"⚠ Warning: {result.stderr}\n")
            else:
                print(f"⚠ Warning: {result.stderr}\n")
    except Exception as e:
        print(f"⚠ Could not generate console report: {e}\n")
    
    print("="*80)
    print(" "*25 + "REPORT GENERATION COMPLETE")
    print("="*80)
    print("\n📂 Generated Reports:")
    print("  • HTML Report: models/TRAINING_RESULTS.html (open in browser)")
    print("  • Markdown Report: models/TRAINING_RESULTS.md (if generated)")
    print("\n")


if __name__ == '__main__':
    main()
