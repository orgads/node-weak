{
  'targets': [
    {
      'target_name': 'weakref',
      'sources': [ 'src/weakref.cc' ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': ['weakref'],
      'copies': [{
        'files': ['<(PRODUCT_DIR)/weakref.node'],
        'destination': 'out',
      }],
    },
  ]
}
