# Import Active Directory module
Import-Module ActiveDirectory

# Define User Information
$givenName = "Franz"
$surname = "Ferdinand"
$sAMAccountName = "fferdinand"
$email = "ferdi@GlobeXpower.com"
$department = "TPS Department"
$location = "Springfield, OR"
$company = "GlobeX USA"
$title = "TPS Reporting Lead"

# Create user object
$newUser = New-ADUser -Name "$givenName $surname" -SamAccountName $sAMAccountName -EmailAddress $email -Title $title -Department $department -Company $company -Location $location -Path "OU=Springfield,OU=USA,DC=GlobeX,DC=com"

# Set password (optional)
# Set-ADUser -Identity $newUser -ChangePasswordOnFirstLogin $true

# Test user creation
Write-Host "User '$newUser' created successfully!"

# Verify user in ADAC
Get-ADUser -Identity $sAMAccountName | Select-Object Name, EmailAddress, Title, Department, Company, Location

# Optional: Delete user if necessary
# Remove-ADUser -Identity $sAMAccountName

# Note: Replace "OU=Springfield,OU=USA,DC=GlobeX,DC=com" with your actual AD organizational unit path.
