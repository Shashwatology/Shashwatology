#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 2600})
        await page.goto("file:///D:/github%20readme/preview.html", wait_until="networkidle")
        
        # Dark screenshot
        await page.emulate_media(color_scheme='dark')
        await page.evaluate("document.body.classList.remove('light')")
        await page.evaluate("""
            document.querySelectorAll('picture').forEach(p => {
                const darkSrc = p.querySelector('source[media*="dark"]')?.getAttribute('srcset');
                const img = p.querySelector('img');
                if (darkSrc && img) {
                    img.src = darkSrc;
                }
            });
        """)
        await page.screenshot(path="assets/preview_dark.png", full_page=True)
        print("Wrote assets/preview_dark.png")
        
        # Light screenshot
        await page.emulate_media(color_scheme='light')
        await page.evaluate("document.body.classList.add('light')")
        await page.evaluate("""
            document.querySelectorAll('picture').forEach(p => {
                const img = p.querySelector('img');
                if (img) {
                    img.src = img.src.replace('-dark.svg', '-light.svg');
                }
            });
        """)
        await page.screenshot(path="assets/preview_light.png", full_page=True)
        print("Wrote assets/preview_light.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
