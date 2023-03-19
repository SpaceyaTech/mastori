# Description

Please include a summary of the changes and the related issue. Please also include relevant motivation and context. List any dependencies that are required for this change.

Fixes # (issue)

## Type of change

Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] This change requires a documentation update

## How Has This Been Tested?

[![CI Django & Postgres Tests](https://github.com/SpaceyaTech/blog/actions/workflows/django-postgres-ci.yml/badge.svg)](https://github.com/SpaceyaTech/blog/actions/workflows/django-postgres-ci.yml)

[![Jambo](https://github.com/SpaceyaTech/mastori/actions/workflows/jambo.yaml/badge.svg)](https://github.com/SpaceyaTech/mastori/actions/workflows/jambo.yaml)


**Test Configuration**:

```sql
          python manage.py migrate
          python manage.py test
```

## Checklist:

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules

