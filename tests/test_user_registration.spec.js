const { test, expect } = require('@playwright/test');

test('User Registration Form Display', async ({ page }) => {
    await page.goto('/register/');
    await expect(page.locator('input[name="username"]')).toBeVisible();
    await expect(page.locator('input[name="first_name"]')).toBeVisible();
    await expect(page.locator('input[name="last_name"]')).toBeVisible();
    await expect(page.locator('input[name="email"]')).toBeVisible();
    await expect(page.locator('input[name="password1"]')).toBeVisible();
    await expect(page.locator('input[name="password2"]')).toBeVisible();
    await expect(page.locator('button[type="submit"]')).toBeVisible();
});

test('User Registration Valid Data', async ({ page }) => {
    await page.goto('/register/');
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="first_name"]', 'Test');
    await page.fill('input[name="last_name"]', 'User');
    await page.fill('input[name="email"]', 'testuser@example.com');
    await page.fill('input[name="password1"]', 'TestPassword123!');
    await page.fill('input[name="password2"]', 'TestPassword123!');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Account created for testuser! Please log in.')).toBeVisible();
});

test('User Registration Password Validation', async ({ page }) => {
    await page.goto('/register/');
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="first_name"]', 'Test');
    await page.fill('input[name="last_name"]', 'User');
    await page.fill('input[name="email"]', 'testuser@example.com');
    await page.fill('input[name="password1"]', '12345');
    await page.fill('input[name="password2"]', '12345');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=This password is too short. It must contain at least 8 characters.')).toBeVisible();
});

test('User Registration Password Mismatch', async ({ page }) => {
    await page.goto('/register/');
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="first_name"]', 'Test');
    await page.fill('input[name="last_name"]', 'User');
    await page.fill('input[name="email"]', 'testuser@example.com');
    await page.fill('input[name="password1"]', 'TestPassword123!');
    await page.fill('input[name="password2"]', 'TestPassword124!');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=The two password fields didn\'t match.')).toBeVisible();
});

test('User Registration Confirmation Message', async ({ page }) => {
    await page.goto('/register/');
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="first_name"]', 'Test');
    await page.fill('input[name="last_name"]', 'User');
    await page.fill('input[name="email"]', 'testuser@example.com');
    await page.fill('input[name="password1"]', 'TestPassword123!');
    await page.fill('input[name="password2"]', 'TestPassword123!');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Account created for testuser! Please log in.')).toBeVisible();
});
